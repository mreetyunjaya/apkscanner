import framework

from androguard.core.bytecodes import dvm
from androguard.core.analysis.analysis import *
from androguard.decompiler.dad import decompile
import re


class Module(framework.module):
    def __init__(self, apk, avd):
        super(Module, self).__init__(apk, avd)
        self.info = {
            "Name": "Javascript explicitly enabled webviews",
            "Author": "Quentin Kaiser (@QKaiser)",
            "Description": "This module will detect if the application explicitly enable javascript within webviews.",
            "Comments": []
        }

    def module_run(self, verbose=False):

        webviews = []

        d = dvm.DalvikVMFormat(self.apk.get_dex())
        dx = VMAnalysis(d)

        z = dx.tainted_packages.search_methods(".", "setJavaScriptEnabled", ".")
        for p in z:
            method = d.get_method_by_idx(p.get_src_idx())
            if method.get_code() is None:
                continue
            mx = dx.get_method(method)
            ms = decompile.DvMethod(mx)
            ms.process()
            source = ms.get_source()

            matches = re.findall(r'setJavaScriptEnabled\((1|true)\)', source)
            if len(matches) == 1:
                webviews.append({
                    "file": method.get_class_name()[1:-1],
                    "line": method.get_debug().get_line_start(),
                })

        return {
            "results": webviews,
            "logs": "",
            "vulnerabilities": [framework.Vulnerability(
                "Explicitly enabled Javascript in WebViews",
                "The application explicitly enable Javascript or Plugins for multiple webviews. This could augment "
                "the attack surface of the application if:\n\t1) The application do not perform certificate validation/"
                "pinning\n\t2)The content loaded through these webviews is vulnerable to cross-site scripting attacks.",
                framework.Vulnerability.LOW
            ).__dict__] if len(webviews) else []
        }
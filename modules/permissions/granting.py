import framework

from androguard.core.bytecodes import dvm
from androguard.core.analysis.analysis import *


permissions = {
    "android.permission.SEND_SMS": {"protection_level": "dangerous"},
    "android.permission.SEND_RESPOND_VIA_MESSAGE": {"protection_level": "signature|system"},
    "android.permission.RECEIVE_SMS": {"protection_level": "dangerous"},
    "android.permission.RECEIVE_MMS": {"protection_level": "dangerous"},
    "android.permission.RECEIVE_EMERGENCY_BROADCAST": {"protection_level": "signature|system"},
    "android.permission.READ_CELL_BROADCASTS": {"protection_level": "dangerous"},
    "android.permission.READ_SMS": {"protection_level": "dangerous"},
    "android.permission.WRITE_SMS": {"protection_level": "dangerous"},
    "android.permission.RECEIVE_WAP_PUSH": {"protection_level": "dangerous"},
    "android.permission.RECEIVE_BLUETOOTH_MAP": {"protection_level": "signature|system"},
    "android.permission.READ_CONTACTS": {"protection_level": "dangerous"},
    "android.permission.WRITE_CONTACTS": {"protection_level": "dangerous"},
    "android.permission.BIND_DIRECTORY_SEARCH": {"protection_level": "signature|system"},
    "android.permission.READ_CALL_LOG": {"protection_level": "dangerous"},
    "android.permission.WRITE_CALL_LOG": {"protection_level": "dangerous"},
    "android.permission.READ_SOCIAL_STREAM": {"protection_level": "dangerous"},
    "android.permission.WRITE_SOCIAL_STREAM": {"protection_level": "dangerous"},
    "android.permission.READ_PROFILE": {"protection_level": "dangerous"},
    "android.permission.WRITE_PROFILE": {"protection_level": "dangerous"},
    "android.permission.BODY_SENSORS": {},
    "android.permission.READ_CALENDAR": {"protection_level": "dangerous"},
    "android.permission.WRITE_CALENDAR": {"protection_level": "dangerous"},
    "android.permission.READ_USER_DICTIONARY": {"protection_level": "dangerous"},
    "android.permission.WRITE_USER_DICTIONARY": {"protection_level": "normal"},
    "com.android.browser.permission.READ_HISTORY_BOOKMARKS": {"protection_level": "dangerous"},
    "com.android.browser.permission.WRITE_HISTORY_BOOKMARKS": {"protection_level": "dangerous"},
    "com.android.alarm.permission.SET_ALARM": {"protection_level": "normal"},
    "com.android.voicemail.permission.ADD_VOICEMAIL": {"protection_level": "dangerous"},
    "com.android.voicemail.permission.WRITE_VOICEMAIL": {"protection_level": "system|signature"},
    "com.android.voicemail.permission.READ_VOICEMAIL": {"protection_level": "system|signature"},
    "android.permission.ACCESS_FINE_LOCATION": {"protection_level": "dangerous"},
    "android.permission.ACCESS_COARSE_LOCATION": {"protection_level": "dangerous"},
    "android.permission.ACCESS_MOCK_LOCATION": {"protection_level": "dangerous"},
    "android.permission.ACCESS_LOCATION_EXTRA_COMMANDS": {"protection_level": "normal"},
    "android.permission.INSTALL_LOCATION_PROVIDER": {"protection_level": "signature|system"},
    "android.permission.HDMI_CEC": {"protection_level": "signatureOrSystem"},
    "android.permission.LOCATION_HARDWARE": {"protection_level": "signature|system"},
    "android.permission.INTERNET": {"protection_level": "dangerous"},
    "android.permission.ACCESS_NETWORK_STATE": {"protection_level": "normal"},
    "android.permission.ACCESS_WIFI_STATE": {"protection_level": "normal"},
    "android.permission.CHANGE_WIFI_STATE": {"protection_level": "dangerous"},
    "android.permission.READ_WIFI_CREDENTIAL": {"protection_level": "signature|system"},
    "android.permission.ACCESS_WIMAX_STATE": {"protection_level": "normal"},
    "android.permission.CHANGE_WIMAX_STATE": {"protection_level": "dangerous"},
    "android.permission.SCORE_NETWORKS": {"protection_level": "signature|system"},
    "android.permission.BLUETOOTH": {"protection_level": "dangerous"},
    "android.permission.BLUETOOTH_ADMIN": {"protection_level": "dangerous"},
    "android.permission.BLUETOOTH_PRIVILEGED": {"protection_level": "system|signature"},
    "android.permission.BLUETOOTH_MAP": {"protection_level": "signature"},
    "android.permission.BLUETOOTH_STACK": {"protection_level": "signature"},
    "android.permission.NFC": {"protection_level": "dangerous"},
    "android.permission.CONNECTIVITY_INTERNAL": {"protection_level": "signature|system"},
    "android.permission.RECEIVE_DATA_ACTIVITY_CHANGE": {"protection_level": "signature|system"},
    "android.permission.LOOP_RADIO": {"protection_level": "signature|system"},
    "android.permission.NFC_HANDOVER_STATUS": {"protection_level": "signature|system"},
    "android.permission.GET_ACCOUNTS": {"protection_level": "normal"},
    "android.permission.AUTHENTICATE_ACCOUNTS": {"protection_level": "dangerous"},
    "android.permission.USE_CREDENTIALS": {"protection_level": "dangerous"},
    "android.permission.MANAGE_ACCOUNTS": {"protection_level": "dangerous"},
    "android.permission.ACCOUNT_MANAGER": {"protection_level": "signature"},
    "android.permission.CHANGE_WIFI_MULTICAST_STATE": {"protection_level": "dangerous"},
    "android.permission.VIBRATE": {"protection_level": "normal"},
    "android.permission.FLASHLIGHT": {"protection_level": "normal"},
    "android.permission.WAKE_LOCK": {"protection_level": "normal"},
    "android.permission.TRANSMIT_IR": {"protection_level": "normal"},
    "android.permission.MODIFY_AUDIO_SETTINGS": {"protection_level": "normal"},
    "android.permission.MANAGE_USB": {"protection_level": "signature|system"},
    "android.permission.ACCESS_MTP": {"protection_level": "signature|system"},
    "android.permission.HARDWARE_TEST": {"protection_level": "signature"},
    "android.permission.NET_ADMIN": {"protection_level": "signature"},
    "android.permission.REMOTE_AUDIO_PLAYBACK": {"protection_level": "signature"},
    "android.permission.TV_INPUT_HARDWARE": {"protection_level": "signatureOrSystem"},
    "android.permission.CAPTURE_TV_INPUT": {"protection_level": "signatureOrSystem"},
    "android.permission.OEM_UNLOCK_STATE": {"protection_level": "signature"},
    "android.permission.RECORD_AUDIO": {"protection_level": "dangerous"},
    "android.permission.CAMERA": {"protection_level": "dangerous"},
    "android.permission.CAMERA_DISABLE_TRANSMIT_LED": {"protection_level": "signature|system"},
    "android.permission.PROCESS_OUTGOING_CALLS": {"protection_level": "dangerous"},
    "android.permission.MODIFY_PHONE_STATE": {"protection_level": "signature|system"},
    "android.permission.READ_PHONE_STATE": {"protection_level": "dangerous"},
    "android.permission.READ_PRECISE_PHONE_STATE": {"protection_level": "signature|system"},
    "android.permission.READ_PRIVILEGED_PHONE_STATE": {"protection_level": "signature|system"},
    "android.permission.CALL_PHONE": {"protection_level": "dangerous"},
    "android.permission.USE_SIP": {"protection_level": "dangerous"},
    "android.permission.BIND_INCALL_SERVICE": {"protection_level": "system|signature"},
    "android.permission.BIND_CONNECTION_SERVICE": {"protection_level": "system|signature"},
    "android.permission.CONTROL_INCALL_EXPERIENCE": {"protection_level": "system|signature"},
    "android.permission.READ_EXTERNAL_STORAGE": {"protection_level": "normal"},
    "android.permission.WRITE_EXTERNAL_STORAGE": {"protection_level": "dangerous"},
    "android.permission.WRITE_MEDIA_STORAGE": {"protection_level": "signature|system"},
    "android.permission.MANAGE_DOCUMENTS": {"protection_level": "signature"},
    "android.permission.DISABLE_KEYGUARD": {"protection_level": "dangerous"},
    "android.permission.GET_TASKS": {"protection_level": "normal"},
    "android.permission.REAL_GET_TASKS": {"protection_level": "signature|system"},
    "android.permission.START_TASKS_FROM_RECENTS": {"protection_level": "signature|system"},
    "android.permission.INTERACT_ACROSS_USERS": {"protection_level": "signature|system|development"},
    "android.permission.INTERACT_ACROSS_USERS_FULL": {"protection_level": "signature"},
    "android.permission.MANAGE_USERS": {"protection_level": "signature|system"},
    "android.permission.GET_DETAILED_TASKS": {"protection_level": "signature"},
    "android.permission.REORDER_TASKS": {"protection_level": "normal"},
    "android.permission.REMOVE_TASKS": {"protection_level": "signature"},
    "android.permission.MANAGE_ACTIVITY_STACKS": {"protection_level": "signature|system"},
    "android.permission.START_ANY_ACTIVITY": {"protection_level": "signature"},
    "android.permission.RESTART_PACKAGES": {"protection_level": "normal"},
    "android.permission.KILL_BACKGROUND_PROCESSES": {"protection_level": "normal"},
    "android.permission.SYSTEM_ALERT_WINDOW": {"protection_level": "dangerous"},
    "android.permission.SET_WALLPAPER": {"protection_level": "normal"},
    "android.permission.SET_WALLPAPER_HINTS": {"protection_level": "normal"},
    "android.permission.SET_TIME": {"protection_level": "signature|system"},
    "android.permission.SET_TIME_ZONE": {"protection_level": "normal"},
    "android.permission.EXPAND_STATUS_BAR": {"protection_level": "normal"},
    "com.android.launcher.permission.INSTALL_SHORTCUT": {"protection_level": "dangerous"},
    "com.android.launcher.permission.UNINSTALL_SHORTCUT": {"protection_level": "dangerous"},
    "android.permission.READ_SYNC_SETTINGS": {"protection_level": "normal"},
    "android.permission.WRITE_SYNC_SETTINGS": {"protection_level": "normal"},
    "android.permission.READ_SYNC_STATS": {"protection_level": "normal"},
    "android.permission.SET_SCREEN_COMPATIBILITY": {"protection_level": "signature"},
    "android.permission.ACCESS_ALL_EXTERNAL_STORAGE": {"protection_level": "signature"},
    "android.permission.CHANGE_CONFIGURATION": {"protection_level": "signature|system|development"},
    "android.permission.WRITE_SETTINGS": {"protection_level": "normal"},
    "android.permission.WRITE_GSERVICES": {"protection_level": "signature|system"},
    "android.permission.FORCE_STOP_PACKAGES": {"protection_level": "signature|system"},
    "android.permission.RETRIEVE_WINDOW_CONTENT": {"protection_level": "signature|system"},
    "android.permission.SET_ANIMATION_SCALE": {"protection_level": "signature|system|development"},
    "android.permission.PERSISTENT_ACTIVITY": {"protection_level": "normal"},
    "android.permission.GET_PACKAGE_SIZE": {"protection_level": "normal"},
    "android.permission.SET_PREFERRED_APPLICATIONS": {"protection_level": "signature"},
    "android.permission.RECEIVE_BOOT_COMPLETED": {"protection_level": "normal"},
    "android.permission.BROADCAST_STICKY": {"protection_level": "normal"},
    "android.permission.MOUNT_UNMOUNT_FILESYSTEMS": {"protection_level": "system|signature"},
    "android.permission.MOUNT_FORMAT_FILESYSTEMS": {"protection_level": "system|signature"},
    "android.permission.ASEC_ACCESS": {"protection_level": "signature"},
    "android.permission.ASEC_CREATE": {"protection_level": "signature"},
    "android.permission.ASEC_DESTROY": {"protection_level": "signature"},
    "android.permission.ASEC_MOUNT_UNMOUNT": {"protection_level": "signature"},
    "android.permission.ASEC_RENAME": {"protection_level": "signature"},
    "android.permission.WRITE_APN_SETTINGS": {"protection_level": "signature|system"},
    "android.permission.SUBSCRIBED_FEEDS_READ": {"protection_level": "normal"},
    "android.permission.SUBSCRIBED_FEEDS_WRITE": {"protection_level": "dangerous"},
    "android.permission.CHANGE_NETWORK_STATE": {"protection_level": "normal"},
    "android.permission.CLEAR_APP_CACHE": {"protection_level": "dangerous"},
    "android.permission.ALLOW_ANY_CODEC_FOR_PLAYBACK": {"protection_level": "signature|system"},
    "android.permission.MANAGE_CA_CERTIFICATES": {"protection_level": "signature|system"},
    "android.permission.RECOVERY": {"protection_level": "signature|system"},
    "android.permission.BIND_JOB_SERVICE": {"protection_level": "signature"},
    "android.permission.WRITE_SECURE_SETTINGS": {"protection_level": "signature|system|development"},
    "android.permission.DUMP": {"protection_level": "signature|system|development"},
    "android.permission.READ_LOGS": {"protection_level": "signature|system|development"},
    "android.permission.SET_DEBUG_APP": {"protection_level": "signature|system|development"},
    "android.permission.SET_PROCESS_LIMIT": {"protection_level": "signature|system|development"},
    "android.permission.SET_ALWAYS_FINISH": {"protection_level": "signature|system|development"},
    "android.permission.SIGNAL_PERSISTENT_PROCESSES": {"protection_level": "signature|system|development"},
    "android.permission.DIAGNOSTIC": {"protection_level": "signature"},
    "android.permission.STATUS_BAR": {"protection_level": "signature|system"},
    "android.permission.STATUS_BAR_SERVICE": {"protection_level": "signature"},
    "android.permission.FORCE_BACK": {"protection_level": "signature"},
    "android.permission.UPDATE_DEVICE_STATS": {"protection_level": "signature|system"},
    "android.permission.GET_APP_OPS_STATS": {"protection_level": "signature|system|development"},
    "android.permission.UPDATE_APP_OPS_STATS": {"protection_level": "signature|system"},
    "android.permission.INTERNAL_SYSTEM_WINDOW": {"protection_level": "signature"},
    "android.permission.MANAGE_APP_TOKENS": {"protection_level": "signature"},
    "android.permission.FREEZE_SCREEN": {"protection_level": "signature"},
    "android.permission.INJECT_EVENTS": {"protection_level": "signature"},
    "android.permission.FILTER_EVENTS": {"protection_level": "signature"},
    "android.permission.RETRIEVE_WINDOW_TOKEN": {"protection_level": "signature"},
    "android.permission.FRAME_STATS": {"protection_level": "signature"},
    "android.permission.TEMPORARY_ENABLE_ACCESSIBILITY": {"protection_level": "signature"},
    "android.permission.SET_ACTIVITY_WATCHER": {"protection_level": "signature"},
    "android.permission.SHUTDOWN": {"protection_level": "signature|system"},
    "android.permission.STOP_APP_SWITCHES": {"protection_level": "signature|system"},
    "android.permission.GET_TOP_ACTIVITY_INFO": {"protection_level": "signature"},
    "android.permission.READ_INPUT_STATE": {"protection_level": "signature"},
    "android.permission.BIND_INPUT_METHOD": {"protection_level": "signature"},
    "android.permission.BIND_ACCESSIBILITY_SERVICE": {"protection_level": "signature"},
    "android.permission.BIND_PRINT_SERVICE": {"protection_level": "signature"},
    "android.permission.BIND_NFC_SERVICE": {"protection_level": "signature"},
    "android.permission.BIND_PRINT_SPOOLER_SERVICE": {"protection_level": "signature"},
    "android.permission.BIND_TEXT_SERVICE": {"protection_level": "signature"},
    "android.permission.BIND_VPN_SERVICE": {"protection_level": "signature"},
    "android.permission.BIND_WALLPAPER": {"protection_level": "signature|system"},
    "android.permission.BIND_VOICE_INTERACTION": {"protection_level": "signature"},
    "android.permission.MANAGE_VOICE_KEYPHRASES": {"protection_level": "signature|system"},
    "android.permission.BIND_REMOTE_DISPLAY": {"protection_level": "signature"},
    "android.permission.BIND_TV_INPUT": {"protection_level": "signature|system"},
    "android.permission.MODIFY_PARENTAL_CONTROLS": {"protection_level": "signature|system"},
    "android.permission.BIND_DEVICE_ADMIN": {"protection_level": "signature"},
    "android.permission.MANAGE_DEVICE_ADMINS": {"protection_level": "signature|system"},
    "android.permission.SET_ORIENTATION": {"protection_level": "signature"},
    "android.permission.SET_POINTER_SPEED": {"protection_level": "signature"},
    "android.permission.SET_INPUT_CALIBRATION": {"protection_level": "signature"},
    "android.permission.SET_KEYBOARD_LAYOUT": {"protection_level": "signature"},
    "android.permission.INSTALL_PACKAGES": {"protection_level": "signature|system"},
    "android.permission.CLEAR_APP_USER_DATA": {"protection_level": "signature"},
    "android.permission.DELETE_CACHE_FILES": {"protection_level": "signature|system"},
    "android.permission.DELETE_PACKAGES": {"protection_level": "signature|system"},
    "android.permission.MOVE_PACKAGE": {"protection_level": "signature|system"},
    "android.permission.CHANGE_COMPONENT_ENABLED_STATE": {"protection_level": "signature|system"},
    "android.permission.GRANT_REVOKE_PERMISSIONS": {"protection_level": "signature"},
    "android.permission.ACCESS_SURFACE_FLINGER": {"protection_level": "signature"},
    "android.permission.READ_FRAME_BUFFER": {"protection_level": "signature|system"},
    "android.permission.ACCESS_INPUT_FLINGER": {"protection_level": "signature"},
    "android.permission.CONFIGURE_WIFI_DISPLAY": {"protection_level": "signature"},
    "android.permission.CONTROL_WIFI_DISPLAY": {"protection_level": "signature"},
    "android.permission.CAPTURE_AUDIO_OUTPUT": {"protection_level": "signature|system"},
    "android.permission.CAPTURE_AUDIO_HOTWORD": {"protection_level": "signature|system"},
    "android.permission.MODIFY_AUDIO_ROUTING": {"protection_level": "signature|system"},
    "android.permission.CAPTURE_VIDEO_OUTPUT": {"protection_level": "signature|system"},
    "android.permission.CAPTURE_SECURE_VIDEO_OUTPUT": {"protection_level": "signature|system"},
    "android.permission.MEDIA_CONTENT_CONTROL": {"protection_level": "signature|system"},
    "android.permission.BRICK": {"protection_level": "signature"},
    "android.permission.REBOOT": {"protection_level": "signature|system"},
    "android.permission.DEVICE_POWER": {"protection_level": "signature"},
    "android.permission.USER_ACTIVITY": {"protection_level": "signature|system"},
    "android.permission.NET_TUNNELING": {"protection_level": "signature"},
    "android.permission.FACTORY_TEST": {"protection_level": "signature"},
    "android.permission.BROADCAST_PACKAGE_REMOVED": {"protection_level": "signature"},
    "android.permission.BROADCAST_SMS": {"protection_level": "signature"},
    "android.permission.BROADCAST_WAP_PUSH": {"protection_level": "signature"},
    "android.permission.BROADCAST_SCORE_NETWORKS": {"protection_level": "signature|system"},
    "android.permission.MASTER_CLEAR": {"protection_level": "signature|system"},
    "android.permission.CALL_PRIVILEGED": {"protection_level": "signature|system"},
    "android.permission.PERFORM_CDMA_PROVISIONING": {"protection_level": "signature|system"},
    "android.permission.CONTROL_LOCATION_UPDATES": {"protection_level": "signature|system"},
    "android.permission.ACCESS_CHECKIN_PROPERTIES": {"protection_level": "signature|system"},
    "android.permission.PACKAGE_USAGE_STATS": {"protection_level": "signature|development|appop"},
    "android.permission.BATTERY_STATS": {"protection_level": "signature|system|development"},
    "android.permission.BACKUP": {"protection_level": "signature|system"},
    "android.permission.CONFIRM_FULL_BACKUP": {"protection_level": "signature"},
    "android.permission.BIND_REMOTEVIEWS": {"protection_level": "signature|system"},
    "android.permission.BIND_APPWIDGET": {"protection_level": "signature|system"},
    "android.permission.BIND_KEYGUARD_APPWIDGET": {"protection_level": "signature|system"},
    "android.permission.MODIFY_APPWIDGET_BIND_PERMISSIONS": {"protection_level": "signature|system"},
    "android.permission.CHANGE_BACKGROUND_DATA_SETTING": {"protection_level": "signature"},
    "android.permission.GLOBAL_SEARCH": {"protection_level": "signature|system"},
    "android.permission.GLOBAL_SEARCH_CONTROL": {"protection_level": "signature"},
    "android.permission.READ_SEARCH_INDEXABLES": {"protection_level": "signature|system"},
    "android.permission.SET_WALLPAPER_COMPONENT": {"protection_level": "signature|system"},
    "android.permission.READ_DREAM_STATE": {"protection_level": "signature|system"},
    "android.permission.WRITE_DREAM_STATE": {"protection_level": "signature|system"},
    "android.permission.ACCESS_CACHE_FILESYSTEM": {"protection_level": "signature|system"},
    "android.permission.COPY_PROTECTED_DATA": {"protection_level": "signature"},
    "android.permission.CRYPT_KEEPER": {"protection_level": "signature|system"},
    "android.permission.READ_NETWORK_USAGE_HISTORY": {"protection_level": "signature|system"},
    "android.permission.MANAGE_NETWORK_POLICY": {"protection_level": "signature"},
    "android.permission.MODIFY_NETWORK_ACCOUNTING": {"protection_level": "signature|system"},
    "android.intent.category.MASTER_CLEAR.permission.C2D_MESSAGE": {"protection_level": "signature"},
    "android.permission.PACKAGE_VERIFICATION_AGENT": {"protection_level": "signature|system"},
    "android.permission.BIND_PACKAGE_VERIFIER": {"protection_level": "signature"},
    "android.permission.SERIAL_PORT": {"protection_level": "signature|system"},
    "android.permission.ACCESS_CONTENT_PROVIDERS_EXTERNALLY": {"protection_level": "signature"},
    "android.permission.UPDATE_LOCK": {"protection_level": "signatureOrSystem"},
    "android.permission.ACCESS_NOTIFICATIONS": {"protection_level": "signature|system"},
    "android.permission.ACCESS_KEYGUARD_SECURE_STORAGE": {"protection_level": "signature"},
    "android.permission.CONTROL_KEYGUARD": {"protection_level": "signature"},
    "android.permission.TRUST_LISTENER": {"protection_level": "signature"},
    "android.permission.PROVIDE_TRUST_AGENT": {"protection_level": "signatureOrSystem"},
    "android.permission.LAUNCH_TRUST_AGENT_SETTINGS": {"protection_level": "signatureOrSystem"},
    "android.permission.BIND_TRUST_AGENT": {"protection_level": "signature"},
    "android.permission.BIND_NOTIFICATION_LISTENER_SERVICE": {"protection_level": "signature"},
    "android.permission.BIND_CONDITION_PROVIDER_SERVICE": {"protection_level": "signature"},
    "android.permission.BIND_DREAM_SERVICE": {"protection_level": "signature"},
    "android.permission.INVOKE_CARRIER_SETUP": {"protection_level": "signature|system"},
    "android.permission.ACCESS_NETWORK_CONDITIONS": {"protection_level": "signature|system"},
    "android.permission.ACCESS_DRM_CERTIFICATES": {"protection_level": "signature|system"},
    "android.permission.MANAGE_MEDIA_PROJECTION": {"protection_level": "signature"},
    "android.permission.READ_INSTALL_SESSIONS": {},
    "android.permission.REMOVE_DRM_CERTIFICATES": {"protection_level": "signature|system"}
}


class Module(framework.module):
    def __init__(self, apk, avd):
        framework.module.__init__(self, apk, avd)
        self.info = {
            "Name": "Permissions analyzer",
            "Author": "Quentin Kaiser (@QKaiser)",
            "Description": "This module compares the permissions asked by the application in the application manifest "
                           "and the permissions actually used by the application to detect undergranting or overgranting"
                           "of permission.",
            "Comments": [
                "Right now, this module is only checking android.permissions permissions and not application defined"
                " permissions."
            ]
        }

    def module_run(self, verbose=False):

        #TODO: the real issue is that "is the code linked to a permission really reached during runtime ?"
        logs = ""
        vulnerabilities = []

        d = dvm.DalvikVMFormat(self.apk.get_dex())
        dx = VMAnalysis(d)
        d.set_vmanalysis(dx)

        results = {
            "manifest_permissions": self.get_permissions(),
            "app_permissions": ["android.permission.%s" % (str(p)) for p in dx.get_permissions([])]
        }
        perms = dx.get_permissions([])
        for perm in perms:
            t=False
            for path in perms[perm]:
                if isinstance(path, PathP):
                    method = d.get_method_by_idx(path.get_src_idx())
                    if self.apk.get_package() in method.get_class_name().replace("/", "."):
                        if method.get_code() is None:
                            continue
                        print method.get_class_name()
                        t=True
            if not t:
                perms[perm] = None

        if verbose:
            print "Manifest permissions:"
            for permission in results["manifest_permissions"]:
                print "\t%s" % permission
            print "App permissions:"
            for permission in results["app_permissions"]:
                print "\t%s" % permission

        undergranting = [x for x in results["app_permissions"]
                         if x in permissions and permissions[x]["protection_level"] != "normal" and x not in results["manifest_permissions"]]
        overgranting = [x for x in results["manifest_permissions"]
                        if x in permissions and permissions[x]["protection_level"] != "normal" and x not in results["app_permissions"]]

        if len(undergranting):
            vulnerabilities.append(framework.Vulnerability(
                "Application permissions undergranting.",
                "The application is using permissions that have not been requested in the application manifest. "
                "This could lead to application error and security hazard."
                "The following permissions are undergranted:\n%s" % ("\n".join(undergranting)),
                framework.Vulnerability.LOW
            ).__dict__)

        if len(overgranting):
            vulnerabilities.append(framework.Vulnerability(
                "Application permissions overgranting.",
                "The application is requesting more permissions than needed in the manifest. While it is not really a"
                "vulnerability, this behaviour is not good."
                "The following permissions are overgranted:\n%s" % ("\n".join(overgranting)),
                framework.Vulnerability.LOW
            ).__dict__)

        return {
            "results": results,
            "logs": logs,
            "vulnerabilities": vulnerabilities
        }
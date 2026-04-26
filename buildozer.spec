[app]

# (str) Title of your application
title = Sara AI

# (str) Package name
package.name = saraai

# (str) Package domain (needed for android packaging)
package.domain = org.imalsha

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.0,google-generativeai,gTTS,requests,urllib3,charset-normalizer,idna,certifi,yarl,multidict,openssl

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = armeabi-v7a, arm64-v8a

# (bool) Accept SDK license
android.accept_sdk_license = True

# (str) python-for-android branch to use
p4a.branch = master

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1

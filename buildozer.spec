[app]
title = Sara AI
package.name = saraai
package.domain = org.imalsha
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy==2.3.0,google-generativeai,gTTS,requests,urllib3,charset-normalizer,idna,certifi,yarl,multidict,openssl

orientation = portrait
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android Settings
# Warning එක මගහරින්න SDK එක මෙතනින් අයින් කරා, එතකොට auto-select වෙනවා
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
android.accept_sdk_license = True

# Broken pipe ප්‍රශ්නයට විසඳුම
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

[app]
title = Sara AI
package.name = saraai
package.domain = org.imalsha
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requirements වලට මේ ටික විතරක් දාන්න
requirements = python3,kivy==2.3.0,google-generativeai,gTTS,requests,urllib3,charset-normalizer,idna,certifi,yarl,multidict,openssl

orientation = portrait
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android Settings (මේවා හරියටම තියෙන්න ඕනේ)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
android.accept_sdk_license = True

# Compile error එක මගහරවා ගන්න මේ පේළිය අනිවාර්යයි
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

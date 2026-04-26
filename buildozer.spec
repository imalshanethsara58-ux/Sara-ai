[app]

# (section) ඇප් එකේ නම සහ විස්තර
title = Sara AI
package.name = saraai
package.domain = org.imalsha
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# (section) අවශ්‍ය කරන Libraries (මේක ගොඩක් වැදගත්)
# සාරාට අවශ්‍ය Gemini සහ gTTS මෙතන තියෙනවා
requirements = python3,kivy==2.3.0,google-generativeai,gTTS,requests,urllib3,charset-normalizer,idna,certifi,yarl,multidict

orientation = portrait

# (section) Permissions
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (section) Android Settings (GitHub එකට ගැළපෙන ඒවා)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True

# (section) මේක 'True' කරන්න අනිවාර්යයෙන්ම (License ප්‍රශ්නය විසඳන්න)
android.accept_sdk_license = True

# (section) Python settings
python_api = 27

[buildozer]
log_level = 2
warn_on_root = 1

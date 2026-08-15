[app]

# اسم التطبيق
title = Sendar Lite

# اسم الحزمة
package.name = sendarlite

# معرّف التطبيق
package.domain = org.sendar

# مكان ملفات التطبيق
source.dir = .

# الملفات التي تدخل داخل APK
source.include_exts = py,png,jpg,jpeg,kv,atlas

# إصدار التطبيق
version = 1.0.0

# المكتبات المطلوبة
requirements = python3,kivy

# اتجاه الشاشة
orientation = portrait

# إظهار شريط الحالة
fullscreen = 0

# صلاحية الإنترنت
android.permissions = INTERNET

# قبول تراخيص Android تلقائيًا
android.accept_sdk_license = True

# إصدار Android المستهدف
android.api = 35

# أقل إصدار Android
android.minapi = 24

# NDK
android.ndk = 28c

# API المستخدم مع NDK
android.ndk_api = 24

# المعمارية
android.archs = arm64-v8a,armeabi-v7a

# مستوى السجل
log_level = 2

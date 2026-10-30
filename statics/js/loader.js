document.addEventListener("DOMContentLoaded", function () {
  const loader = document.getElementById("page-loader");

  function showLoader() {
    if (loader) {
      loader.classList.remove("loader-hidden");
    }
  }

  function hideLoader() {
    if (loader) {
      loader.classList.add("loader-hidden");
    }
  }

  // ۱. وقتی صفحه لود شد، لودر مخفی بشه
  window.addEventListener("load", function () {
    // ۲۰۰ میلی‌ثانیه تاخیر نرم برای تجربه کاربری بهتر
    setTimeout(hideLoader, 200);
  });

  // ۲. جلوگیری از گیر کردن لودر موقع زدن دکمه Back یا Forward مرورگر
  window.addEventListener("pageshow", function (event) {
    hideLoader();
  });

  // ۳. هندل کردن کلیک روی لینک‌های منو و صفحات
  document.addEventListener("click", function (event) {
    const link = event.target.closest("a");

    if (!link) return;

    const href = link.getAttribute("href");

    // اگر لینک به بالا پرش می‌کنه، دکمه جاوااسکریپتیه یا خالیه
    if (!href || href.startsWith("#") || href.startsWith("javascript:") || href === "") {
      return;
    }

    // اگر کاربر لینک رو توی تب جدید باز کرد (مثلا با کلیک راست یا target="_blank")
    if (link.target === "_blank" || event.ctrlKey || event.metaKey) {
      return;
    }

    // بررسی اینکه آیا لینک مربوط به همین سایت است؟
    try {
      const targetUrl = new URL(link.href, window.location.href);

      // لینک به سایت دیگه‌ای میره
      if (targetUrl.origin !== window.location.origin) return;

      // اگر کاربر روی لینک صفحه‌ای که دقیقاً توش هست کلیک کرد
      if (targetUrl.href === window.location.href) return;

      // نمایش لودر برای انتقال به صفحه جدید
      showLoader();
    } catch (e) {
      // آدرس نامعتبر بود
    }
  }, true);

  // ۴. موقع سابمیت فرم‌ها هم لودر نشون داده بشه (اختیاری ولی به شدت کاربردی برای فرم‌های ثبت‌نام/لاگین)
  document.addEventListener("submit", function (event) {
    const form = event.target;
    // اگر فرم target="_blank" نداره لودر رو نشون بده
    if (form.target !== "_blank") {
      showLoader();
    }
  });
});



document.addEventListener("submit", function (event) {
  const form = event.target;
  // چک می‌کنه اگر فرم خطای اعتبارسنجی (مثل فیلد خالی اجباری) داره، لودر نیاد
  if (form.checkValidity && !form.checkValidity()) {
    return;
  }

  if (form.target !== "_blank") {
    showLoader();
  }
});



// These codes are made by ai (Gemini)
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

  // ۱. مخفی شدن با لود کامل صفحه
  window.addEventListener("load", function () {
    setTimeout(hideLoader, 200);
  });

  // ۲. هندل کردن دکمه Back/Forward مرورگر
  window.addEventListener("pageshow", function () {
    hideLoader();
  });

  // ۳. هندل کردن لینک‌ها
  document.addEventListener("click", function (event) {
    const link = event.target.closest("a");
    if (!link) return;

    const href = link.getAttribute("href");
    if (!href || href.startsWith("#") || href.startsWith("javascript:") || href === "") return;
    if (link.target === "_blank" || event.ctrlKey || event.metaKey) return;

    try {
      const targetUrl = new URL(link.href, window.location.href);
      if (targetUrl.origin !== window.location.origin) return;
      if (targetUrl.href === window.location.href) return;

      showLoader();
    } catch (e) {}
  }, true);

  // ۴. هندل کردن هوشمند فرم‌ها
  document.addEventListener("submit", function (event) {
    const form = event.target;

    // الف) اگر فرم نامعتبره (مثلا فیلد required پر نشده)، لودر نیاد
    if (form.checkValidity && !form.checkValidity()) {
      return;
    }

    // ب) با تاخیر ۵۰ میلی‌ثانیه چک کن آیا واقعا فرم داره سابمیت میشه؟
    // اگر JS دیگه‌ای جلوش رو با preventDefault گرفته باشه، لودر نمایش داده نمیشه
    setTimeout(function () {
      if (!event.defaultPrevented && form.target !== "_blank") {
        showLoader();

        // ج) تایم‌اوت نجات (Fail-safe): 
        // اگر بعد از ۱۵ ثانیه به هر دلیلی صفحه رفرش نشد، لودر رو ببند تا صفحه قفل نشه
        setTimeout(function () {
          hideLoader();
        }, 15000);
      }
    }, 50);
  });
});

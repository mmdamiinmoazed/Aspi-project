(function () {
    // تابع قطع و مخفی کردن اجباری لودر
    function forceHideLoader() {
        const loader = document.getElementById("page-loader");
        if (loader) {
            loader.style.setProperty("display", "none", "important");
            loader.classList.add("loader-hidden");
        }
    }

    // ۱. بلافاصله در لحظه اجرا، لودر رو مخفی کن
    forceHideLoader();

    // ۲. در تمام مراحل آماده‌شدن صفحه مطمئن شو لودر بسته است
    document.addEventListener("DOMContentLoaded", forceHideLoader);
    window.addEventListener("load", forceHideLoader);
    window.addEventListener("pageshow", forceHideLoader);

    // ۳. تایمر برای نمایش با تاخیر
    let loaderTimeout = null;

    function triggerLoader() {
        clearTimeout(loaderTimeout);
        // تاخیر ۴۰۰ میلی‌ثانیه: اگر لود سریع بود اصلاً ظاهر نشه
        loaderTimeout = setTimeout(function () {
            const loader = document.getElementById("page-loader");
            if (loader) {
                loader.style.setProperty("display", "flex", "important");
                loader.classList.remove("loader-hidden");
            }
        }, 400);

        // سوپاپ اطمینان: اگر تا ۸ ثانیه صفحه عوض نشد، خودکار لودر بسته بشه تا گیر نکنه
        setTimeout(forceHideLoader, 8000);
    }

    // ۴. فقط روی لینک‌های واقعی و معتبر کار کنه
    document.addEventListener("click", function (e) {
        const link = e.target.closest("a");
        if (!link) return;

        const href = link.getAttribute("href");

        // نادیده گرفتن لینک‌های پوچ، داخلی یا پنجره جدید
        if (
            !href ||
            href.startsWith("#") ||
            href.startsWith("javascript:") ||
            link.getAttribute("target") === "_blank" ||
            e.ctrlKey || e.metaKey || e.shiftKey
        ) {
            return;
        }

        triggerLoader();
    });

    // ۵. فرم‌ها (فقط فرم‌هایی که ولیدیشن موفق دارن)
    document.addEventListener("submit", function (e) {
        if (e.defaultPrevented) return;
        const form = e.target;
        if (form && !form.checkValidity()) return;

        triggerLoader();
    });
})();

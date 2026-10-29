const loader = document.getElementById("page-loader");

// وقتی صفحه کاملاً بارگذاری شد
window.addEventListener("load", () => {
    loader.classList.remove("active");
});

// هنگام کلیک روی لینک‌های داخلی
document.addEventListener("click", (event) => {
    const link = event.target.closest("a");

    if (!link) return;

    if (
        link.target === "_blank" ||
        link.hasAttribute("download") ||
        event.ctrlKey ||
        event.shiftKey ||
        event.altKey ||
        event.metaKey
    ) return;

    const url = new URL(link.href);

    if (url.origin !== window.location.origin) return;

    if (
        link.href.includes("#") &&
        url.pathname === window.location.pathname
    ) return;

    if (link.getAttribute("href") === "javascript:void(0)") return;

    // فقط لینک‌های معمولی GET
    showLoader();
});

function showLoader() {
    loader.classList.add("active");
}

function hideLoader() {
    loader.classList.remove("active");
}
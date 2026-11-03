document.addEventListener('DOMContentLoaded', function () {
  const commentForm = document.getElementById('project-comment-form');
  const commentBtn = document.getElementById('comment-submit-btn');
  const commentError = document.getElementById('comment-error');

  if (!commentForm) {
    console.error("خطای حیاتی: المان با آیدی project-comment-form پیدا نشد!");
    return;
  }

  // تابع کمکی تمیز برای مدیریت نمایش ارور
  function showError(msg) {
    if (commentError) {
      commentError.textContent = msg;
      commentError.style.display = 'block';
    }
  }

  function clearError() {
    if (commentError) {
      commentError.textContent = '';
      commentError.style.display = 'none';
    }
  }

  if (commentBtn) {
    commentBtn.addEventListener('click', async function (e) {
      e.preventDefault();


      clearError();

      const commentInput = document.getElementById('comment-text');
      const commentText = commentInput ? commentInput.value.trim() : '';

      // ۲. اعتبارسنجی کلاینت (اگر خالی بود ارور رو بفرست به تگ p)
      if (!commentText) {
        showError("متن نظر نمی‌تواند خالی باشد.");
        return;
      }

      const csrfEl = commentForm.querySelector('[name=csrfmiddlewaretoken]');
      const csrfToken = csrfEl ? csrfEl.value : '';
      const targetUrl = commentForm.getAttribute('action');

      try {
        const response = await fetch(targetUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
            'X-Requested-With': 'XMLHttpRequest'
          },
          body: JSON.stringify({ comment: commentText })
        });

        const data = await response.json();

        // ۳. بررسی پاسخ سرور
        if (response.ok && data.status === 'success') {
          clearError();
          window.location.reload(); 
        } else {
          // دریافت مستقیم پیام خطایی که بک‌اند جنگو فرستاده
          const serverError = data.message || "خطایی در ثبت نظر رخ داد.";
          showError(serverError);
        }
      } catch (err) {
        console.error("خطا در ارسال Fetch:", err);
        showError("ارتباط با سرور برقرار نشد. لطفاً اینترنت خود را بررسی کنید.");
      }
    });
  }
});

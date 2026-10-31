
document.addEventListener('DOMContentLoaded', function () {
  const voteForm = document.getElementById('project-vote-form');
  if (!voteForm) return;

  const buttons = voteForm.querySelectorAll('.vote__btn');

  buttons.forEach(button => {
    button.addEventListener('click', async function (e) {
      e.preventDefault();

      const voteType = this.getAttribute('data-vote');
      const targetUrl = voteForm.getAttribute('action');
      const csrfToken = voteForm.querySelector('[name=csrfmiddlewaretoken]').value;

      console.log('Sending vote:', voteType, 'to:', targetUrl);

      try {
        const response = await fetch(targetUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
            'X-Requested-With': 'XMLHttpRequest'
          },
          body: JSON.stringify({ action: voteType })
        });

        if (response.status === 401) {
          alert('برای ثبت رأی ابتدا باید وارد حساب کاربری خود شوید.');
          return;
        }

        const data = await response.json();
        console.log('Server response:', data);

        if (response.ok && data.status === 'success') {
          // بروزرسانی شمارنده‌ها در DOM
          const likeCount = voteForm.querySelector('[data-vote="like"] .vote__count');
          const dislikeCount = voteForm.querySelector('[data-vote="dislike"] .vote__count');

          if (likeCount && data.likes !== undefined) likeCount.textContent = data.likes;
          if (dislikeCount && data.dislikes !== undefined) dislikeCount.textContent = data.dislikes;

          // وضعیت فعال بودن دکمه‌ها
          const likeBtn = voteForm.querySelector('[data-vote="like"]');
          const dislikeBtn = voteForm.querySelector('[data-vote="dislike"]');

          const islike = (data.user_vote === 'like' || data.user_vote === 'like');
          const isdislike = (data.user_vote === 'dislike' || data.user_vote === 'dislike');

          likeBtn.setAttribute('aria-pressed', islike);
          likeBtn.classList.toggle('is-active', islike);

          dislikeBtn.setAttribute('aria-pressed', isdislike);
          dislikeBtn.classList.toggle('is-active', isdislike);
        }
      } catch (error) {
        console.error('Fetch error:', error);
      }
    });
  });
});

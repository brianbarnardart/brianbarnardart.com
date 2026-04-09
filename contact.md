---
layout: page
title: Contact
permalink: /contact/
nav: false
---

Interested in a piece, a commission, or just want to say hello?

You can reach me at **[Facebook: @brianbarnardart](https://www.facebook.com/brianbarnardart/)** or on **[LinkedIn](https://www.linkedin.com/in/brian-barnard-60b7b543)**, or use the form below!

<form id="contact-form" action="https://api.formspark.io/AvqUDoWyl" method="POST" class="contact-form" novalidate>
  <div class="form-field">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" placeholder="Your name" required>
  </div>
  <div class="form-field">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="your@email.com">
  </div>
  <div class="form-field">
    <label for="phone">Phone <span class="optional">(optional)</span></label>
    <input type="tel" id="phone" name="phone" placeholder="(555) 555-5555">
  </div>
  <div class="form-field">
    <label for="message">Message</label>
    <textarea id="message" name="message" placeholder="What's on your mind?" required></textarea>
  </div>
  <button type="submit" class="form-submit">Send Message</button>
  <p id="form-status" class="form-status" aria-live="polite"></p>
</form>

<script>
  // Auto-grow textarea
  const msg = document.getElementById('message');
  msg.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
  });

  // AJAX submission — stay on page, show inline result
  const form = document.getElementById('contact-form');
  const status = document.getElementById('form-status');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const submitBtn = form.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending…';
    status.textContent = '';
    status.className = 'form-status';

    const data = new FormData(form);

    fetch(form.action, {
      method: 'POST',
      body: data,
      headers: { 'Accept': 'application/json' }
    })
    .then(function (res) {
      if (res.ok) {
        form.reset();
        msg.style.height = '';
        status.textContent = 'Message sent — thank you! Brian will be in touch soon.';
        status.classList.add('form-status--ok');
      } else {
        throw new Error('server error');
      }
    })
    .catch(function () {
      status.textContent = 'Something went wrong. Please try again or contact Brian on Facebook.';
      status.classList.add('form-status--err');
    })
    .finally(function () {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Send Message';
    });
  });
</script>

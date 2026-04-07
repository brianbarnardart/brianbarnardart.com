---
layout: page
title: Contact
permalink: /contact/
---

Interested in a piece, a commission, or just want to say hello?

You can reach me at **[Facebook: @brianbarnardart](https://www.facebook.com/brianbarnardart/)** or on **[LinkedIn](https://www.linkedin.com/in/brian-barnard-60b7b543)**, and soon I'll have the form below working too.  :-)

<form action="https://submit.formspark.io/f/FORMSPARK_FORM_ID" method="POST" class="contact-form">
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
</form>

<script>
  const msg = document.getElementById('message');
  msg.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
  });
</script>

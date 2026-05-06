---
layout: page
title: Privacy
description: Your Privacy Matters
permalink: /privacy/
image: /assets/icons/astro-death-head.png
---

# Your Visit... *Your Business*

This site respects your privacy.  (Did you notice your browser didn't have to ask "Accept Cookies?")  It collects minimal, anonymous click counts.  And you can turn even that off, right here, right now.

**For this browser:** <span id="counting-status">checking…</span>

<p>
  <button id="counting-off" class="form-submit">Turn counters OFF</button>
  <button id="counting-on" class="form-submit">Turn counters ON</button>
</p>

<p id="counting-confirm" aria-live="polite"></p>


## What data is collected?

{% include figure.html image="/assets/icons/astro-death-head.png" side="right" link="https://themarkup.org/blacklight/2020/09/22/what-they-know-now" %}

This site uses **[GoatCounter](https://www.goatcounter.com/)** for basic analytics — things like which pages are visited and roughly where visitors come from (by country, not address). That's it.

GoatCounter does **not**:

- Use cookies
- Track you across other websites
- Build an advertising profile on you
- Sell your data to anyone
- Share your data with Google, Meta, or any other third party

GoatCounter is open source, independently operated, and funded by its users — not by selling your attention or your data.


### Why GoatCounter instead of Google Analytics?

The short version: **Google Analytics is free because *you* are the product.**

Google Analytics gives site owners detailed visitor data in exchange for Google receiving that data too — adding it to the profile Google builds on you *across every site that uses it*.

GoatCounter is open source and allows you to run it on your own servers.  For smaller sites like this one, they also offer a community-funded service where they store your data of what's being clicked for you (but still not the personal profile of the person who visited it).

This site uses GoatCounter because understanding which pages people visit is genuinely useful — but not at the cost of your privacy.


### Contact form submissions

When you use the contact form, your name, email address, and message are sent to **[FormSpark](https://formspark.io/)** (a form processing service) and forwarded to Brian's email. A record that the form was submitted is also logged in GoatCounter — including your email address in the event title — as a backup to catch any messages that may not have gotten through.

This is the only case where personally identifiable information appears in analytics.  (But you typed it in and pushed a 'send' button, so...not that surprising that it was sent somewhere!  Having GoatCounter record that fact just helps double-check that the middlemen actually passed it on to Brian.)


### Embedded YouTube videos

The video clips on this site are embedded using YouTube's **privacy-enhanced mode** (`youtube-nocookie.com`). With standard YouTube embeds, YouTube sets cookies in your browser the moment the page loads — even if you never touch the video. The nocookie domain changes that: no cookies are set until you actually click play.

Once you do play a video, YouTube will know it was watched (that's unavoidable with any streaming service), but it won't have been silently tracking your visit just because the page loaded.


### Turning off counting

The button at the top of this page sets a flag in your browser's local storage (`skipgc = t`). GoatCounter's script checks for this flag and skips counting your visits when it is set. No data is sent. The flag stays set until you turn counting back on, or until you clear your browser's local storage for `brianbarnardart.com`.

(This is also useful for the site developers to turn off self-views so that their own visits don't inflate the traffic numbers.)

<script>
(function () {
  var status = document.getElementById('counting-status');
  var confirm = document.getElementById('counting-confirm');
  var btnOff = document.getElementById('counting-off');
  var btnOn = document.getElementById('counting-on');

  function isSkipping() {
    return localStorage.getItem('skipgc') === 't';
  }

  function updateStatus() {
    if (isSkipping()) {
      status.textContent = 'OFF — this browser is not being counted.';
      btnOff.disabled = true;
      btnOn.disabled = false;
    } else {
      status.textContent = 'ON — this browser is being counted.';
      btnOff.disabled = false;
      btnOn.disabled = true;
    }
  }

  btnOff.addEventListener('click', function () {
    localStorage.setItem('skipgc', 't');
    confirm.textContent = 'Counting turned OFF. GoatCounter will no longer count visits from this browser.';
    updateStatus();
  });

  btnOn.addEventListener('click', function () {
    localStorage.removeItem('skipgc');
    confirm.textContent = 'Counting turned ON. GoatCounter will count visits from this browser again.';
    updateStatus();
  });

  updateStatus();
}());
</script>

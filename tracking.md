---
layout: default
title: Analytics Tracking
---

## Analytics Tracking

This page shows and controls whether GoatCounter analytics are recorded in this browser.  It's primarily intended for turning off tracking in browsing for Brian Barnard himself (or website developers) so that self-views don't get counted as site traffic!

**Current status:** <span id="tracking-status">checking…</span>

<p>
  <button id="tracking-off" class="form-submit">Turn tracking OFF</button>
  <button id="tracking-on" class="form-submit">Turn tracking ON</button>
</p>

<p id="tracking-confirm" aria-live="polite"></p>

<script>
(function () {
  var status = document.getElementById('tracking-status');
  var confirm = document.getElementById('tracking-confirm');
  var btnOff = document.getElementById('tracking-off');
  var btnOn = document.getElementById('tracking-on');

  function isSkipping() {
    return localStorage.getItem('skipgc') === 't';
  }

  function updateStatus() {
    if (isSkipping()) {
      status.textContent = 'OFF — this browser is not being tracked.';
      btnOff.disabled = true;
      btnOn.disabled = false;
    } else {
      status.textContent = 'ON — this browser is being tracked.';
      btnOff.disabled = false;
      btnOn.disabled = true;
    }
  }

  btnOff.addEventListener('click', function () {
    localStorage.setItem('skipgc', 't');
    confirm.textContent = 'Tracking turned OFF. GoatCounter will no longer count visits from this browser.';
    updateStatus();
  });

  btnOn.addEventListener('click', function () {
    localStorage.removeItem('skipgc');
    confirm.textContent = 'Tracking turned ON. GoatCounter will count visits from this browser again.';
    updateStatus();
  });

  updateStatus();
}());
</script>

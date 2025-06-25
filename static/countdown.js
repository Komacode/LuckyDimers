window.COUNTDOWN_TARGET_DATE = "2025-06-30T00:00:00";

const countdownDate = new Date(window.COUNTDOWN_TARGET_DATE);

const updateCountdown = () => {
  const now = new Date();

  if (now >= countdownDate) {
    document.querySelector('.countdown-wrapper').innerHTML = "<div class='label'>¡Ya está disponible!</div>";
    return;
  }

  let temp = new Date(now);
  let months = 0;
  while (temp < countdownDate) {
    temp.setMonth(temp.getMonth() + 1);
    if (temp <= countdownDate) {
      months++;
    } else {
      break;
    }
  }
  temp.setMonth(temp.getMonth() - 1);

  const remainingMs = countdownDate - temp;
  const days = Math.floor(remainingMs / (1000 * 60 * 60 * 24));
  const hours = Math.floor((remainingMs % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((remainingMs % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((remainingMs % (1000 * 60)) / 1000);

  document.getElementById("months").textContent = String(months).padStart(2, '0');
  document.getElementById("days").textContent = String(days).padStart(2, '0');
  document.getElementById("hours").textContent = String(hours).padStart(2, '0');
  document.getElementById("minutes").textContent = String(minutes).padStart(2, '0');
  document.getElementById("seconds").textContent = String(seconds).padStart(2, '0');
};

updateCountdown();
setInterval(updateCountdown, 1000);

// Add keyboard support and a localized name to the library's scroll control.
addBackToTop({
  scrollDuration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 100,
});

const backToTop = document.getElementById("back-to-top");
backToTop.setAttribute("role", "button");
backToTop.setAttribute("aria-label", document.documentElement.lang === "fr" ? "Retour en haut" : "Back to top");
backToTop.querySelector("svg").setAttribute("aria-hidden", "true");

const updateBackToTopVisibility = () => {
  const hidden = backToTop.classList.contains("hidden");
  backToTop.tabIndex = hidden ? -1 : 0;
  backToTop.setAttribute("aria-hidden", String(hidden));
};

backToTop.addEventListener("keydown", (event) => {
  if (event.key === "Enter" || event.key === " ") {
    event.preventDefault();
    backToTop.click();
  }
});
backToTop.addEventListener("click", () => {
  document.getElementById("main-content")?.focus({ preventScroll: true });
});
window.addEventListener("scroll", updateBackToTopVisibility, { passive: true });
updateBackToTopVisibility();

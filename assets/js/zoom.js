// Native gallery viewer with keyboard focus and Escape handling.
$(document).ready(function () {
  const galleryButtons = document.querySelectorAll(".image-zoom-button");
  const otherImages = Array.from(document.querySelectorAll("[data-zoomable]")).filter((image) => !image.closest(".image-zoom-button"));
  medium_zoom = mediumZoom(otherImages, {
    background: getComputedStyle(document.documentElement).getPropertyValue("--global-bg-color").trim() + "ee",
  });
  if (!galleryButtons.length) return;

  const french = document.documentElement.lang === "fr";
  const viewer = document.createElement("dialog");
  viewer.className = "image-viewer";
  viewer.setAttribute("aria-label", french ? "Image agrandie" : "Enlarged image");
  const closeButton = document.createElement("button");
  closeButton.type = "button";
  closeButton.className = "image-viewer-close";
  closeButton.textContent = french ? "Fermer" : "Close";
  const image = document.createElement("img");
  viewer.append(closeButton, image);
  document.body.append(viewer);
  let activeButton;

  galleryButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const thumbnail = button.querySelector("img");
      // Use the full source, not the density-corrected responsive thumbnail.
      image.src = thumbnail.getAttribute("data-zoom-src") || thumbnail.src;
      image.alt = thumbnail.alt;
      activeButton = button;
      button.setAttribute("aria-expanded", "true");
      viewer.showModal();
    });
  });

  closeButton.addEventListener("click", () => viewer.close());
  viewer.addEventListener("click", (event) => {
    if (event.target === viewer || event.target === image) viewer.close();
  });
  viewer.addEventListener("close", () => {
    activeButton?.setAttribute("aria-expanded", "false");
    activeButton?.focus({ preventScroll: true });
    image.removeAttribute("src");
  });
});

// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-research",
          title: "research",
          description: "Research in Kähler geometry, complex geometry, geometric analysis, and canonical metrics.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "Teaching at UQAM in Montréal, including MAT0339 General Mathematics, calculus, linear algebra, and introductory university mathematics.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "Academic CV of Xia Xiao, PhD candidate in mathematics at UQAM.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-travel",
          title: "travel",
          description: "Snapshots from long-distance hiking and cycling adventures.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/travel/";
          },
        },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "projects-educational-mathematics-video-series",
          title: 'Educational Mathematics Video Series',
          description: "French educational mathematics videos built with Python and Manim for visually clean explanations of university-level and curriculum topics.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/math-video/";
            },},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];

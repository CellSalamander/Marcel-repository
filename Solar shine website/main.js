

const slides = [
  {
    heading : "Meet the team",
    text: "At the heart of our business is a passionate team of professionals dedicated to delivering top-quality solar panel cleaning services. With a focus on safety, efficiency, and customer satisfaction, our technicians are trained to handle every job with care and precision. We're a small but mighty team that takes pride in helping homeowners and businesses get the most out of their solar energy systems.",
    image: "images/slideimage1.jpg"
  },
  {
    heading : "We are located in Pretoria",
    text: "Proudly serving the greater Pretoria area, we’re a locally owned and operated business that understands the unique needs of our community. Whether you're in the city or surrounding suburbs, we’re just a call away and ready to keep your solar panels performing at their best.",
    image: "images/slideimage2.jpg"
  },
  {
    heading : "Since 2020",
    text: "Since opening our doors in 2020, we've built a reputation for reliable, professional service and long-term customer relationships. What started as a small venture has grown into a trusted name in solar panel care, thanks to our commitment to quality and consistent results.",
    image: "images/slideimage3.jpg"
  }
];

let currentSlide = 0;

document.getElementById("slideHeading").textContent = slides[currentSlide].heading;
document.getElementById("slideshow-text").textContent = slides[currentSlide].text;
document.getElementById("slideshow-image").src = slides[currentSlide].image;

document.getElementById("next-btn").addEventListener("click", () => {
  currentSlide = (currentSlide + 1) % slides.length;
  document.getElementById("slideHeading").textContent = slides[currentSlide].heading;
  document.getElementById("slideshow-text").textContent = slides[currentSlide].text;
  document.getElementById("slideshow-image").src = slides[currentSlide].image;
});


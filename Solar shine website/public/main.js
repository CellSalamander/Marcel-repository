
document.querySelectorAll('.navbar_links a').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    findlinks(link);
  });
});

function findlinks(link){
  targetSection = false
  targetID = link.getAttribute('href').substring(1);
  targetSection = document.getElementById(targetID);
  if (targetSection){
    targetSection.scrollIntoView({behavior: 'smooth'});
  }
}

btnContact = document.getElementById('btnContact');
btnContact.addEventListener('click', viewContact);

function viewContact(){
  contactSection = document.getElementById('contact')
  contactSection.scrollIntoView({behavior: 'smooth'})
}

const slides = [
  {
    heading : "Before and After",
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


btnBook = document.getElementById("btnBook");
btnBook.addEventListener('click', makeBooking)

async function makeBooking(){


  const formData = {
    name: document.getElementById('name').value,
    surname: document.getElementById('surname').value,
    phone: document.getElementById('phone').value,
    email: document.getElementById('email').value,
    address: document.getElementById('address').value,
    message: document.getElementById('message').value
  };

  for (let key in formData) {
    if (!isSafe(formData[key])) {
      alert("Your input contains potentially unsafe characters.");
      return;
    }
  }

  try {
    const response = await fetch('http://localhost:3000/api/book', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });

    const result = await response.json();
    if (response.ok) {
      alert("Booking successful!");
    } else {
      alert("Booking failed: " + result.error);
    }

  } catch (err) {
      console.error("Fetch error:", err);
      alert("Something went wrong.");
    }

}

function isSafe(input){
  const blacklist = /(\b(SELECT|INSERT|DELETE|UPDATE|DROP|UNION|--|;|\/\*|\*\/|xp_)\b|['"])/i;
  if (blacklist.test(input)){
    return false
  }
  else{
    return true
  }
}




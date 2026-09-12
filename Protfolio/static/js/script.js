
// ================================
// UNDER DEVELOPMENT LINKS
// ================================
let isphone=false
const devButtons = document.querySelectorAll(".under-dev");

devButtons.forEach((button) => {
    button.addEventListener("click", (event) => {

        // Stop the "#" link from jumping to the top
        event.preventDefault();

        alert("🚧 This project is under development. Coming soon!");
    });
});


// ================================
// DEVICE DETECTION
// ================================

const isMobile = /Android|iPhone|iPad|iPod|Mobile/i.test(
    navigator.userAgent
);

if (isMobile) {

    console.log("📱 Mobile/tablet detected");
isphone=true;
    //alert("⚠️ For the best experience, please use a PC or laptop.");

} else {

    console.log("💻 PC/laptop detected");

}

const quotes = [
    // 🧪 Chemistry
    {
        text: "The important thing is not to stop questioning. Curiosity has its own reason for existing.",
        author: "Albert Einstein"
    },
    {
        text: "Nothing in life is to be feared, it is only to be understood.",
        author: "Marie Curie"
    },
    {
        text: "The discovery of a new dish does more for the happiness of the human race than the discovery of a star.",
        author: "Jean Anthelme Brillat-Savarin"
    },
    {
        text: "Chemistry is necessarily an experimental science.",
        author: "Michael Faraday"
    },
    {
        text: "Chemistry is the study of matter, but I prefer to think of it as the study of change.",
        author: "Walter White"
    },

    // 💻 Computer Science
    {
        text: "What I cannot create, I do not understand.",
        author: "Richard Feynman"
    },
    {
        text: "The best way to predict the future is to invent it.",
        author: "Alan Kay"
    },
    {
        text: "Programs must be written for people to read, and only incidentally for machines to execute.",
        author: "Harold Abelson"
    },
    {
        text: "Computer science is no more about computers than astronomy is about telescopes.",
        author: "Edsger W. Dijkstra"
    },
    {
        text: "Simplicity is prerequisite for reliability.",
        author: "Edsger W. Dijkstra"
    },
    {
        text: "The function of good software is to make the complex appear to be simple.",
        author: "Grady Booch"
    },
    {
        text: "The most disastrous thing that you can ever learn is your first programming language.",
        author: "Alan Kay"
    },

    // 🔬 Science & discovery
    {
        text: "Somewhere, something incredible is waiting to be known.",
        author: "Carl Sagan"
    },
    {
        text: "Science is the great antidote to the poison of enthusiasm and superstition.",
        author: "Adam Smith"
    },
    {
        text: "The science of today is the technology of tomorrow.",
        author: "Edward Teller"
    },
    {
        text: "Research is to see what everybody else has seen, and to think what nobody else has thought.",
        author: "Albert Szent-Györgyi"
    },

    // 🧪💻 Science + technology
    {
        text: "The computer was born to solve problems that did not exist before.",
        author: "Bill Gates"
    },
    {
        text: "The real problem is not whether machines think but whether men do.",
        author: "B. F. Skinner"
    },
    {
        text: "Any sufficiently advanced technology is indistinguishable from magic.",
        author: "Arthur C. Clarke"
    },
    {
        text: "Technology is a word that describes something that doesn't work yet.",
        author: "Douglas Adams"
    }
];

const quoteElement = document.getElementById("quote");
const authorElement = document.getElementById("quote-author");

function showRandomQuote() {

    const randomIndex = Math.floor(Math.random() * quotes.length);

    quoteElement.textContent = `"${quotes[randomIndex].text}"`;
    authorElement.textContent = `- ${quotes[randomIndex].author}`;
}

showRandomQuote();

setInterval(showRandomQuote, 1 * 60 * 300);
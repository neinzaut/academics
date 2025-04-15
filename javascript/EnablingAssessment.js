let library = [

    // first book
    {
        title: "Speaking JavaScript",
        author: "Axel Rouschmayer",
        pages: 460
    },

    // second book
    {
        title: "Programming JavaScript Applications",
        author: "Eric Elliott",
        pages: 254
    },

    // third book
    {
        title: "Understanding ECMAScript6",
        author: "Nicholas C. Zakas",
        pages: 352
    }
];


library.push( // appends to end of list
    {
        title: "Learning JavaScript Design Patterns",
        author: "Addy Osmani",
        pages: 254
    }
);

console.log(library.length);    // prints number of items in list
console.log(library[0].title);
console.log(library[1].title);
console.log(library[2].title);
console.log(library[3].title);
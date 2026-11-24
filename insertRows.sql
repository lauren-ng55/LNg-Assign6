INSERT INTO category (categoryName, categoryImage) VALUES 
('Biography and Memoir', 'biography-memoir-category.jpg'),
('Literary Classics', 'literary-classics-category.jpg'),
('Cooking and Food', 'cooking-food-category.jpg'),
('Self-Help', 'self-help-category.jpg'),
('History', 'history-category.jpg');

INSERT INTO book (categoryId, title, author, isbn, price, bookImage, readNow) VALUES
(1, 'Steve Jobs', 'Walter Isaacson', '978-1-250-01445-0', 15.75, 'steve-jobs-book.jpg', 0),
(1, 'Educated', 'Tara Westover', '978-0-399-59050-4', 29.50, 'educated-book.jpg', 1),
(1, 'The Power Broker', 'Robert Caro', '978-0-394-72024-1', 16.50, 'power-broker-book.jpg', 0),
(2, 'Of Mice and Men', 'John Steinbeck', '978-0-140-17739-8', 14.00, 'of-mice-and-men-book.jpg', 0),
(2, 'The Great Gatsby', 'F. Scott Fitzgerald', '978-1-982-14670-2', 9.50, 'the-great-gatsby-book.jpg', 1),
(2, 'The Catcher in the Rye', 'J. D. Salinger', '978-0-316-76948-8', 10.25, 'the-catcher-in-the-rye-book.jpg', 1),
(3, 'The Gastronomical Me', 'M. F. K. Fisher', '978-0-865-47392-8', 10.50, 'the-gastronomical-me-book.jpg', 0),
(3, 'Librae: Third-culture Recipes from a Cult New York Bakery', 'Dona Murad', '978-1-837-83626-0', 34.50, 'librae-bakery-book.jpg', 0),
(3, 'The Cook You Want to Be: Everyday Recipes to Impress', 'Andy Baraghani', '978-1-984-85856-6', 22.50, 'the-cook-you-want-to-be-book.jpg', 0),
(4, 'Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones', 'James Clear', '978-0-735-21129-2', 21.00, 'atomic-habits-book.jpg', 1),
(4, 'The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change', 'Stephen R. Covey', '978-1-451-63961-2', 17.50, 'the-7-habits-of-highly-effective-people-book.jpg', 0),
(4, 'How to Win Friends and Influence People', 'Dale Carnegie', '978-1-982-017145-2', 31.00, 'how-to-win-friends-and-influence-people-book.jpg', 0),
(5, 'Guns, Germs, and Steel: The Fates of Human Societies', 'Jared Diamond', '978-0-393-31755-8', 25.75, 'guns-germs-and-steel-book.jpg', 1),
(5, 'Hiroshima: The Last Witnesses', 'M. G. Sheftall', '978-0-593-47225-5', 20.00, 'hiroshima-the-last-witnesses-book.jpg', 0),
(5, 'Vanished: An Unnatural History of Extinction', 'Sadiah Qureshi', '978-0-241-35210-6', 27.25, 'vanished-an-unnatural-history-of-extinction-book.jpg', 0);

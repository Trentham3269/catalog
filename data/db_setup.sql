CREATE TABLE categories (  
  id SERIAL PRIMARY KEY,  
  name VARCHAR(50) NOT NULL
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(80) UNIQUE NOT NULL 
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY, 
  title VARCHAR(50) NOT NULL,
  description VARCHAR(250) NOT NULL,
  cat_id INTEGER REFERENCES categories(id),
  user_id INTEGER REFERENCES users(id)
);

INSERT INTO categories (id, name) VALUES (1, 'Soccer');
INSERT INTO categories (id, name) VALUES (2, 'Basketball');
INSERT INTO categories (id, name) VALUES (3, 'Baseball');
INSERT INTO categories (id, name) VALUES (4, 'Frisbee');
INSERT INTO categories (id, name) VALUES (5, 'Snowboarding');
INSERT INTO categories (id, name) VALUES (6, 'Rock Climbing');
INSERT INTO categories (id, name) VALUES (7, 'Football');
INSERT INTO categories (id, name) VALUES (8, 'Surfing');
INSERT INTO categories (id, name) VALUES (9, 'Hockey');

INSERT INTO users (id, email) VALUES (1, 'testuser_one@gmail.com');
INSERT INTO users (id, email) VALUES (2, 'testuser_two@gmail.com');

INSERT INTO items (id, title, description, cat_id, user_id) VALUES (1, 'Boots', 'The latest in comfort, style and cost!', 1, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (2, 'Indoor ball', 'As used in the NBA', 2, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (3, 'Outdoor ball', 'Great for local pickup games', 2, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (4, 'Net', 'The only net for that full swoosh sound', 2, 2);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (5, 'Wooden bat', 'What a beautiful piece of hickory', 3, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (6, 'Ball', 'Handmade - childrens fingers make for exquisite stitching', 3, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (7, 'Frisbee', 'Well...duh!', 4, 2);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (8, 'Snowboard', 'Boutique board made from carbon fibre, the optimum mix of light-weight strength and profit margin', 5, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (9, 'Goggles', 'Wrap around UV protection so you can see when you are being ripped off', 5, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (10, 'Gloves', 'Microfibre lining for warmth and stuff', 5, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (11, 'Rope', 'Supports a climber up to 150kgs (as long as their fingers do)', 6, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (12, 'Rocks', 'Do we really sell these???', 6, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (13, 'Football', 'The good old pigskin', 7, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (14, 'Helmet', 'Best worn before your time in the concussion protocol', 7, 2);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (15, 'Shoulder pads', 'Bigger than those in an 80s sitcom', 7, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (16, 'Surfboard', 'Almost obligatory', 8, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (17, 'Stick', 'Field or ice?', 9, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (18, 'Ice skates', 'Well that explains the stick type', 9, 2);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (19, 'Shin pads', 'Necessary for the times when not faking injury', 1, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (20, 'Mitt', 'Specifically designed for those with butter fingers', 3, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (21, 'Wax', 'Protect what is probably your only investment', 8, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (22, 'Puck', 'Without this hockey could just be called fighting on ice', 9, 2);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (23, 'Ski poles', 'With these you can create a new hybrid sport', 5, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (24, 'Metal bat', 'What a beautiful hunk of metal', 3, 1);
INSERT INTO items (id, title, description, cat_id, user_id) VALUES (25, 'Cleats', 'Engineered by NASA for maximum grip on AstroTurf', 7, 1);

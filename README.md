<h1 align="center">Project title</h1>

we are using, align="center" because we can't use CSS here.

Description
After the title, you must provide a description of the project and it should not be a long paragraph just a simple descriptive line will do the job. This is the line that should be well crafted and straightforward.
It describes the quality of your project because no one will run the project at the moment they visit but they judge the project its description.

# Project Description

or if also like to make it at the center so,

<p align="center">Project Description</p>

Table of Content
Github added this feature already so you don't need to do it. So, Just use headings (#), subheadings(#), or h1,h2 tags and it will automatically have at the top left corner of your README.md file.

Links
Use markdown link as [Link Text](link) of your live project, repo, API, API repo. I am sure you are wondering why you should put repo here but your project is not always be seen on GitHub people also clone it on their system and this file also gets cloned so you must put this link there. So, anyone can visit back the repo.

Include screenshots
You can use Images to show your project, how it looks while running. For putting screenshots you can either drag and drop images or use the image in markdown as ![Image Name](Image location)

How to use your software
The most important part after the description is this, You need to provide instruction on how to install your program and how to run it. Make it comprehensive as much as possible So, even a beginner can use it.

Built With
In this section, you can add your tech stack, as which technologies you used to make the project. You can utilize list as

- JavaScript
- Node
- NPM
- Webpack
- HTML
- CSS
Future updates
Here you can use a Special GFM Feature called a task list. A task list will show which things are done and which are pending. You can utilize a task list as

- [ ] Reliable Storage // This is pending
- [x] Authentication // This is done
Author
Here you can show your details like email, profile, website, any other social media links so others can follow you.
This can be some simple markdown links as

**Rohit Jain**

- [Profile](https://github.com/rohit19060 "Rohit jain")
- [Email](mailto:rohitjain19060@gmail.com?subject=Hi% "Hi!")
- [Website](https://kingtechnologies.in "Welcome")
Contribution
If someone puts effort to do something into your project then you should give him/her credit for it and this is the section for that here you can use images and links of your project contributors.

Support
At last, you can ask for support or sponsorships by providing links or just add a simple message as

Contributions, issues, and feature requests are welcome!
Give a ⭐️ if you like this project!
Template
As I mentioned above you can use the following template as your template after making necessary changes.

<h1 align="center"><project-name></h1>

<p align="center"><project-description></p>

## Links

- [Repo](https://github.com/Rohit19060/<project-name> "<project-name> Repo")

- [Live](<Homepage url> "Live View")

- [Bugs](https://github.com/Rohit19060/<project-name>/issues "Issues Page")

- [API](<API Link> "API")

## Screenshots

![Home Page](/screenshots/1.png "Home Page")

![](/screenshots/2.png)

![](/screenshots/3.png)

## Available Commands

In the project directory, you can run:

### `npm start" : "react-scripts start"`,

The app is built using `create-react-app` so this command Runs the app in Development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser. You also need to run the server file as well to completely run the app. The page will reload if you make edits.
You will also see any lint errors in the console.

### `"npm run build": "react-scripts build"`,

Builds the app for production to the `build` folder. It correctly bundles React in production mode and optimizes the build for the best performance. The build is minified and the filenames include the hashes. Your app will be ready to deploy!

### `"npm run test": "react-scripts test"`,

Launches the test runner in the interactive watch mode.

### `"npm run dev": "concurrently "nodemon server" "npm run start"`,

For running the server and app together I am using concurrently this helps a lot in the MERN application as it runs both the server (client and server) concurrently. So you can work on them both together.

### `"serve": "node server"`

For running the server file on you can use this command.

### `npm run serve`

## Built With

- JavaScript
- Node
- NPM
- Webpack
- HTML
- CSS

## Future Updates

- [ ] Reliable Storage

## Author

**Rohit Jain**

- [Profile](https://github.com/rohit19060 "Rohit jain")
- [Email](mailto:rohitjain19060@gmail.com?subject=Hi "Hi!")
- [Website](https://kingtechnologies.in "Welcome")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
Markdown features
You can also you text styling as
- **Bold**
- _italics_
- ~~Strike through~~
Their combination also works like **_Bold Italics_**

Blockquote
> This is a Blockquote
Lists
- Candy
- Gum
- Booze

1.  Red
2.  Green
3.  Blue

- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
Link
Inline-style link: example link.
Optionally, you may include a title attribute in the parentheses:example link. The title is a text that shows when you hover on an element.

Images
alt text

GFM feature
if you put a link inside arrows like <rohitjain19060@gmail.com> Github automatically make it a link.

Table
| Left-aligned | Center-aligned | Right-aligned |
| :----------- | :------------: | ------------: |
| git status   |   git status   |    git status |
| git diff     |    git diff    |      git diff |
A hidden trick I give sometimes
You can use variables in markdown or references as

![alt text][id]
[id]: /path/to/img.jpg "Title"
This is all you can do in the README.md file to make it stunning and stand out from others. Comment down below your favorite part or your README styles

Let me know if you have any questions or queries. I’ll be happy to help you
Like share, and follow. You can also check my other profiles on King Technologies
Thanks for reading
Discussion (2)
Subscribe
pic

 
incrementis profile image
Akin C.
•
Aug 10 '21

Hello Rohit Jain,

thanks for your article.
It's very informative and I've tried some things you explained in a test repo

I ran into an issue that will not allow me to like and share your article.
Problem is as follows:
Uploading an image using drag and drop saves the image in user-images.githubusercontent.com.
Here is an example:

user-images.githubusercontent.com/...

While looking for a solution, I found the following content on stackoverflow:
Can images on 'user-images.githubusercontent.com' be deleted?

It does not seem possible to delete uploaded images after using drag and drop. I understand this lack of control for the user comes from GitHub.

However, please consider to mention this problem in your article or even offer a solution on how to delete the images so uploaded.
I would love to give a heart and share your article on twitter.

3
 likes

Reply
 
rohit19060 profile image
Rohit Jain   
•
Sep 21 '21

Hi Akin,
Thanks for Reading my blog.

That's raw content, you can upload files in repo and use that instead of using drag n drop, that will give you all the control.

1
 like

Reply
Code of Conduct • Report abuse
Read next
elpddev profile image
Using NX Distributed Execution In Github Actions CI
Eyal Lapid - Jan 7
es404020 profile image
PHP deployment to SSH server using Github action and bash script
es404020 - Dec 29 '21
protium profile image
Publish your blog articles everywhere with this github action
protium - Jan 16
madza profile image
14 GitHub Repositories to Ace Your JavaScript Interviews 🎯 🚀
Madza - Jan 18

Rohit Jain
Follow
Building Web & Mobile Projects and gain a lot of expertise in them. Graphic design is my passion. Like to work in Teams but never hesitate to work alone.
LOCATION
Indian
WORK
Tech Head at King Technologies
JOINED
Apr 23, 2021
Trending on DEV Community  
Wess Cope profile image
Almost Netflix: A Netflix clone built with Flutter + Appwrite
#flutter #showdev #beginners #tutorial
Buddhadeb Chhetri profile image
JavaScript ES6
#javascript #beginners #webdev #productivity
Kira profile image
How to build a REST API using NodeJS
#api #restapi #node #tutorial
<h1 align="center"><project-name></h1>

<p align="center"><project-description></p>

## Links

- [Repo](https://github.com/Rohit19060/<project-name> "<project-name> Repo")

- [Live](<Homepage url> "Live View")

- [Bugs](https://github.com/Rohit19060/<project-name>/issues "Issues Page")

- [API](<API Link> "API")

## Screenshots

![Home Page](/screenshots/1.png "Home Page")

![](/screenshots/2.png)

![](/screenshots/3.png)

## Available Commands

In the project directory, you can run:

### `npm start" : "react-scripts start"`,

The app is built using `create-react-app` so this command Runs the app in Development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser. You also need to run the server file as well to completely run the app. The page will reload if you make edits.
You will also see any lint errors in the console.

### `"npm run build": "react-scripts build"`,

Builds the app for production to the `build` folder. It correctly bundles React in production mode and optimizes the build for the best performance. The build is minified and the filenames include the hashes. Your app will be ready to deploy!

### `"npm run test": "react-scripts test"`,

Launches the test runner in the interactive watch mode.

### `"npm run dev": "concurrently "nodemon server" "npm run start"`,

For running the server and app together I am using concurrently this helps a lot in the MERN application as it runs both the server (client and server) concurrently. So you can work on them both together.

### `"serve": "node server"`

For running the server file on you can use this command.

### `npm run serve`

## Built With

- JavaScript
- Node
- NPM
- Webpack
- HTML
- CSS

## Future Updates

- [ ] Reliable Storage

## Author

**Rohit Jain**

- [Profile](https://github.com/rohit19060 "Rohit jain")
- [Email](mailto:rohitjain19060@gmail.com?subject=Hi "Hi!")
- [Website](https://kingtechnologies.in "Welcome")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
DEV Community — A constructive and inclusive social network for software developers. With you every step of your journey.
Built on Forem — the open source software that powers DEV and other inclusive communities.
Made with love and Ruby on Rails. DEV Community © 2016 - 2022.

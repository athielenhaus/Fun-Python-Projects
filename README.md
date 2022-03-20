# Python Projects

This repo contains a number of Python projects I developed as part of a Udemy course.

## Pong Game
- Uses the Turtle package
- Recreates the classic game where you try to get the ball past your opponents paddle

## Turtle Crossing Game
- Uses the Turtle package
- Recreates the classic game where you are a turtle which has to cross a road without getting hit by a car

## Tkinter Pomodoro Timer
- Uses Tkinter
- The program opens a GUI built with Tkinter, with which the user can manage his or her work sprints and breaks for increased productivity.

## Rain Alert
- Uses the Openweather API as well as Twilio for SMS messaging
- The program checks the weather forecast for your area using the Openweather API
- If the forecast for the next 12 hours includes a high chance of rain, the program sends an SMS alert to your phone telling you to bring an umbrella.

## Stock Trading Alert
- Uses a stock price API, a news API as well as Twilio for SMS messaging
- The program checks the price for the stock you have defined (ex: TESLA) using the stock price API
- If the price of the stock has either risen or fallen by 5% for two consecutive days, the program uses the news API and gets the top 3 stories pertaining to that stock
- The program sends an SMS alert to your phone indicating either the rise or fall of the stock as well as the titles of the 3 news articles

## Top 100 Billboard Scrape 
- Uses BeautifulSoup and the Spotipy API
- The program asks the user to which date in the past the user would like to travel
- The program opens a webpage with the top 100 billboard for the specified date and scrapes it using BeautifulSoup
- The program extracts the artists and song titles from the scraped data and uses them to search Spotify for song tracks, using the Spotipy API
- The program creates a new playlist in the user's Spotify account and adds the identified song tracks

## Cheap Flight Club
- Uses Sheety, Twilio and Tequila APIs. 
- You can enter your desired travel destinations into a spreadsheet, as well as the maximum price you are willing to pay to get there. 
- The program scans the spreadsheet with your destinations and max fares, gets the corresponding airport codes and searches the Tequila API for the cheapest flights to that destination 
- If the cheapest flight is lower than the max fare you are willing to pay, the program sends an SMS alert to your phone using the Twilio API

## LinkedIn Job Application Bot
- Uses Selenium
- The program links in to your LinkedIn account, to a page with EasyApply job search results meeting previously defined criteria (ex: "Barcelona" for location).
- The program applies to each job in the job search results, provided that the menus meet the previously defined pattern. There is limited error handling


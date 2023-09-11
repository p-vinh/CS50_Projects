-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Theft took place on July 28, 2021
-- Humphrey Street

-- First Clue: Humphrey's bakery
SELECT description AS desc, street FROM crime_scene_reports AS csr
WHERE year = 2021
  AND month = 7
  AND day = 28
  AND street = 'Humphrey Street'
  AND desc LIKE '%duck%';

-- Second Clue: Security Cam footage of car
--				Atm transactions
--				Earliest flight out of Fiftyville tomorrow
--				Accomplice bought plane ticket
SELECT name, transcript FROM interviews
WHERE year = 2021
  AND month = 7
  AND day = 28
  AND transcript LIKE '%bakery%';


-- Gives all the license plates that exited the bakery
--
SELECT people.license_plate, people.name, people.phone_number, people.passport_number
FROM bakery_security_logs
	JOIN people
	ON people.license_plate = bakery_security_logs.license_plate

WHERE year = 2021
  AND month = 7
  AND day = 28
  AND hour = 10
  AND minute BETWEEN 15 AND 25
  AND activity = 'exit'
ORDER BY name;


-- Clues on the person withdrawing from the bank on Leggett Street
-- Suspect Bruce
SELECT people.name, atm.account_number, amount
FROM atm_transactions as atm
	JOIN bank_accounts AS bankacc
	  ON bankacc.account_number = atm.account_number
	JOIN people
	  ON people.id = bankacc.person_id


WHERE year = 2021
  AND month = 7
  AND day = 28
  AND atm_location = 'Leggett Street'
  AND transaction_type = 'withdraw';


-- Accomplice Name and phone number. Must make sure by looking at flight purchases
SELECT name, receiver
FROM phone_calls
	JOIN people
	  ON phone_calls.receiver = people.phone_number
WHERE caller = '(367) 555-5533'
  AND year = 2021
  AND month = 7
  AND day = 28
  AND duration < 60;


SELECT full_name, city, abbreviation, hour, minute, seat
FROM flights

JOIN airports ON flights.destination_airport_id = airports.id
JOIN passengers ON passengers.flight_id = flights.id

WHERE year = 2021
  AND month = 7
  AND day = 29
  AND hour < 10
  AND passport_number = 5773159633





puts 2 + 5
# Built-in objects - Data types

#important" To run a ruby on the terminal you have to name it like "ruby name_of_the_file.rb"

#Main methods
#.class told you the class of the variable
#.capitalize transform the first letter in capitalize
#Documentation:https://ruby-doc.org/3.1.2/

#String
puts "london".class
puts "london".capitalize
puts "london".upcase
puts "LoNDon".downcase
puts "london".length
#To know what a method use this line ri String#upcase or ri String#downcase

age = 28
#Concatenation
puts "ruby" + "lecture"
puts "ruby" + " " + "lecture"
puts "I am " + age.to_s + " years old"

#Interpolation
#When you put #{} using strings you can add any ruby code
puts "I am age #{age} years old"

#Integer
puts 42.class
puts 3 + 3
puts 3 -1
puts 3 * 3
puts 11/4

puts 42.0.class
puts 11.0/4
puts 11/4.0
puts 11.0/4.0

puts 11.4.to_i
puts 11.8.round
puts 11.8.floor
puts 11.2.ceil

#When puts ? you always expect a true or false (boolean)
puts 20.even?
puts 20.odd?

#Array list of element
#Syntax for array [] or w%()
puts [].class
puts %w(Huey Dewey Loise).class
puts [].length
puts ["london", "paris"].length
puts %w(Huey Dewey Loise).count
puts %w(Huey Dewey Loise).size
puts %w(Huey Dewey Loise).length
puts %w(Huey Dewey Loise).sort

puts [1, 2, 3, 4, 5, 6, 7, 8, 9]
puts (1..10).class
puts (1..10).to_a
puts (1..100).to_a

#Special Values (booleans)
puts nil
puts false
puts true.class

puts  "How old are you?"
age = gets.chomp.to_i #Ask for a value to the user and convert it to an integer

condition = age >= 18
puts condition

if condition
  puts "You can vote!"
  #What to do if met
else
  puts "You can't vote :("
end
puts "Goobye!"



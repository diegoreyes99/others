# Ternary operator
# condition ? code_when_truly : code_when_falsy

coin = ['heads', 'tails'].sample

puts "Heads o tails?"
choice = gets.chomp
# if choice == coin
#   result = "won"
# else
#   result = "lost"
# end

choice == coin ? result = "won" : result = "lost"

puts "You #{result}!"

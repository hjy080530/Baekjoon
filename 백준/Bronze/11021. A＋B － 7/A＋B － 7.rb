t = gets.to_i

(1..t).each do |i|
  a, b = gets.split.map(&:to_i)
  puts "Case ##{i}: #{a + b}"
end
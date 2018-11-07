require "sinatra"

get "/images/:img.png" do |img|
    res_mod = img.to_i % 5
    halt 404, "There's no such image!" if res_mod == 0
    "You got a 200!"
end
weather_condition =input("What's the weather like today?: (sunny/rainy/cold)").lower()

if weather_condition == "sunny":
 print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
 print("Don't forget your umbrella and raincoat.")
elif weather_condition == "cold":
 print("Make sure to wear a warm coat and a scarf")
else:
 print("Sorry, I dont have recommendations for this weather")


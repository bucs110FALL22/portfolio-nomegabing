# https://hard-drive.net/report-god-saw-everything-you-did-to-your-sims/
# article im using ^

article = "SAN FRANCISCO — An outraged God descended upon the Earth today, and among other things announced that He saw every last thing all of us did to our Sims, concerned sources confirmed. “It’s honestly embarrassing that this would make my list of things to address,” said God, speaking to gathered reporters and worshipers outside of an In-N-Out Burger where He was reportedly really wolfing them down. “But now that I’ve told you who to vote for and which religion got it all the way right, let me just say, what are you people doing to your Sims? Even if they can’t feel anything, the urges you people have, I don’t know. I wonder about this whole thing sometimes, I really do.” While many were obviously panicked by the disapproval of our lord and creator, some boldly alleged hypocrisy on God’s part. “Oh okay, like God’s never let a couple people drown or fuck up their marriage?” asked Lewis Barker, a longtime Sims player. “Sure, I built some walls around my neighbors when they wandered in my backyard and let them starve to death, and yes, I’ve thrown a poisonous dinner party or two. I get how that doesn’t look great, but this is also God. He came up murder and torture and all that in the first place. Give me a break. You don’t have to be THAT judgmental.” Before ascending back to the heavens, God admitted that He would finally be trying The Sims 4 when it goes free to play next month, “to see what all the fuss is about,” assuming He has completed Snipe Elite 5 by then."

substitutions = {
  "God":"the Broski Upstairs",
  "Sims":"Game People",
  "I":"Me",
  "the":"burro",
  "it":"thy",
}

for key,value in substitutions.items():
 article = article.replace(key, value)

print(article)
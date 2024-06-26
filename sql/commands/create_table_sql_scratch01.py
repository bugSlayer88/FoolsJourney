# # figuring out how to best do this table:
# CREATE TABLE card_meaning (
#     card_id SERIAL PRIMARY KEY,
# 	card varchar(100),
# 	base_meaning varchar(800),
#     negative_meaning varchar(800),
# 	major_arcana boolean,
# 	minor_arcana boolean,
# 	court_card boolean
# );
#
# # update table with info:
# INSERT INTO card_meaning(card, base_meaning, negative_meaning, major_arcana, minor_arcana, court_card)
# VALUES

('Fool', 'The Fool evokes an enormous burst of energy. Wherever he goes he brings this vital impulse. Charge forward and let your worries go, trust in the universe and take the plunge.', 'A sense of inconsistency and madness is present. The Fool moves forward regardless of the journey, make sure your efforts are worthy.', 'True', 'False', 'False'),
('Magician', 'A new beginning opens up to you. Make reasoning quick and set your focus. Make your decisions and take action.', 'Beware immaturity and let go of the idea that everything is possible. It is time to make a decision and commit.', 'True', 'False', 'False'),
('High Priestess', 'Stick to your ideals and morality. Maintain discipline, consider sobriety. Prepare the mind and body for the birth of something new.', 'Neglecting ones studies or being too cold and isolated may be a problem here.', 'True', 'False', 'False'),
('Empress', 'Let your creativity guide you. Get inspired, get energized and make your dreams reality.', 'Your female energy is blocked. You may have missed an opportunity recently. If expression is abused or limited the Empress gets resentful and mean. Beware negative views of the feminine.', 'True', 'False', 'False'),
('Emperor', 'The Emperor asks questions of the father figure. How are you expressing your masculine traits? Take action to make you and yours secure.', 'Masculine energy may be blocked. It is time to pony up and work towards your security in the world.', 'True', 'False', 'False'),
('Hierophant', 'Open up to communication. Stick to traditions in action but keep the mind receptive to new lessons. Seek out mentors and teachers.', 'Beware the hypocrisy of your religion. Gurus may be greedy and misleading. It may be time to break away from mentorship.', 'True', 'False', 'False'),
('Lovers', 'Get clear on your emotional state. Take time to question yourself and how you feel. Which character on the card do you associate with currently?', 'Perverse love is risk here. Are you engaging in infedility?', 'True', 'False', 'False'),
('Chariot', 'Beware inflexibility and lack of caution now. A successful conquest can be a reality, particularly in the media.', 'Stop acting with reckless abandon. Question your methods for maneuvering out in the world. Slow down.', 'True', 'False', 'False'),
('Justice', 'Distinguish subjective from objective judgements, learn to clearly say yes and no. Wrap up any political or legal matters. You will get what you deserve.', 'Are you breaking the law? Themes of dictatorship may be present and harmful.', 'True', 'False', 'False'),
('Hermit', 'A change which cannot be avoided and must be accepted faces you. Look to an inner solitude, go to the secret place within you for spiritual transformation.', 'Crisis is afoot. Poverty, decay, solitude may be holding you back.', 'True', 'False', 'False'),
('Wheel of Fortune', 'The only constant in life is change. What goes up must come down. Your luck will turn around.', 'You are resisting change.', 'True', 'False', 'False'),
('Strength', 'Are you holding yourself back? Are you letting your creativity out or reining it in? Embrace your challenges.', 'The part of you that has been suppressed needs attention now.', 'True', 'False', 'False'),
('Hanged Man', 'Do not make decisions now. Inaction will allow your intelligence to ripen. Make this restraint your sacrifice for better opportunity.', 'Unnecessary punishment of the self shold be stopped.', 'True', 'False', 'False'),
('Death', 'There is no birth without death. What do you need to mourn and express to feel peace? Death comes in peace, and wants to take from you that which holds you back. Allow the energy of creation to come forward, if this is not enough - let the revolution out.', 'Internalized anger needs to be expressed. Resisting change is hurting you.', 'True', 'False', 'False'),
('Temperance', 'Introduce positivity to the passions which harm. To dark add light, jealousy to trust. Look at what imbalances you and bring in the opposite. Be cautious of vices.', 'Assess why you are imbalanced. Polarization is harmful now.', 'True', 'False', 'False'),
('Devil', 'Promises of money come in. Examine contracts carefully right now. For questions of creativity - inspiration is within you. In all cases, let your desires guide you but keep your head.', 'Beware routines that trap you. You are blocked creatively and avoiding a project.','True', 'False', 'False'),
('Tower', 'You face potential catastrophe or separation. Something less obvious is trying to reach you - stop looking for God in the sky and find him on Earth.', 'A great change is near.','True', 'False', 'False'),
('Star', 'Luck, prosperity, fertility surround you. You have found your place in life. Where does the Star spill her jars in your life? If it is in the past or into nothingness - how can this be resolved.', 'You are being too demanding and wasting your energy. Watch your attitude - it is potentially poisonous. Do not languish in the past.', 'True', 'False', 'False'),
('Moon', 'Employ feminine qualities now. Lead with receptivity and intuition. Poorly defined anxieties will cause you harm.', 'Mommy issues abound and nightmares are possible.', 'True', 'False', 'False'),
('Sun', 'Good luck on all accounts. Look to the father figure for awakening the soul and the mother figure for intelligence in the heart. The sun gives - take only what you need lest these gifts bring misfortune.', 'Daddy issues may be a factor now. The presence of the Father and your relationship with it affect you.', 'True', 'False', 'False'),
('Judgement', 'Stop going against who you are. Judgements made by humans do not matter right now. Only God can judge you.', 'Do not avoid Spirit. Stop resisting your partner. Dismiss thoughts of self hatred and stop thinking you are unwanted.', 'True', 'False', 'False'),
('World', 'You reach understanding now. A perfect world, a happy marriage, worldly success, successful birth. If the World is at the end of a reading ask what happened in your childhood which is in the way of your success.', 'Your trauma is holding you back. If this appears at the beginning of the reading you have more decisions to make.', 'True', 'False', 'False'),

('Ace of Swords', 'A flash of insight, guidance to simplify the mind, cut the unnecessary. Great intellectual potential and mental capacity (think ten of wands, which is heading to meet this ace). This could indicate a great intellectual victory by using discernment or cunning. It is a good time to decide or take a stance.', 'Negatively it warns of verbal abuse and hurt feelings as well as an overestimation of the minds abilities.', 'False', 'True', 'False'),
('Two of Swords', 'Daydreams, plans, information and theories overflow. So many possibilities for mental accomplishment are present but none have been acted on. The intellect remains passive waiting for action. This can also indicate analysis paralysis.', 'It warns of foolishness, lazy thinking, paralyzing duality and a lack of focus. ', 'False', 'True', 'False'),
('Three of Swords', 'The mind is ready to burst forth and eager to learn. The urge to blurt out first opinions is strong. The intellect is still immature here. The mind is spontaneous and does not discern between believing and knowing. Literally this could signify the desire to pass an exam or achieve some kind of intellectual growth.', 'Beware of fanaticism and abandon half-baked ideas. Be diligent in following up on worthy ideas.', 'False', 'True', 'False'),
('Four of Swords', 'Finally ideas stabilize! Trust in your intellectual maturity. The need to keep thoughts to oneself may be present. A suppression of your ideas may arise and there may be a lack of enthusiasm now. You are being practical but you may be shutting out your heart.', 'Negatively this warns of being too set in ones thinking, the mind becoming a prisoner of its concepts, all bark and no bite and in worst cases tyranny.', 'False', 'True', 'False'),
('Five of Swords', 'A new point of view allows for the understanding of others as well. It is time to resume study, perfect your knowledge and become a specialist. New information will help transform your daily life.', 'Beware being a hypocrite, false understanding of the world, and dangerous polarizing.', 'False', 'True', 'False'),
('Six of Swords', 'The first step into pure joy is taken. We love where our mind is and everything feels like it is blossoming in finesse. Poetry finds its home here. Now is when we meet someone whom offers enriching dialogue.', 'Negatively be warned of self confidence, neglecting to act on the idea of beauty, and narcissism. Attain beauty from within, meditate.', 'False', 'True', 'False'),
('Seven of Swords', 'The growth of our mental state nears its perfection and is receptive to everything. This is a good time to move beyond the self and lend your mind to the greater good. We are mature enough to move beyond the self successfully.', 'Negatively this warns of gossip, using knowledge for cynical purposes and destructive ideas. Lessons in receptivity, remove distractions', 'False', 'True', 'False'),
('Eight of Swords', 'As with all eights we reach a stable perfection and for swords this means emptiness. Great concentration comes easily, like a super power. Meditation allows for the conflict of opposites to merge in celebration of the present. All revelations are possible and answers to problems will come easily. Channel the buddhist void', 'Intellectual blocks, coma, dementia are at play. A fear of emptiness drives you.', 'False', 'True', 'False'),
('Nine of Swords', 'This sword evokes illumination but there is more than meets the eye. Do not let false understanding trick you into thinking you know more than others. it is time to break old mental habits and let go. Listen to others, there are more ideas other than your own.', 'Negatively this speaks to fear of losing ones individuality, depression or even a physical wound to the brain.', 'False', 'True', 'False'),
('Ten of Swords', 'The mind has achieved harmony with the heart, a full understanding is attained. Beware emotional blocks or creating your own negative situations - your mind is very powerful now.', 'Fears of being hurt cause intellectual blocks. Disputes and ingratitude are themes', 'False', 'True', 'False'),
('Page of Swords', 'This Page possesses a good intellectual foundation but lacks self confidence. Perhaps he hasnt finished his education and must move forward with caution.', 'Negatively he warns of lies, confusion, verbal fights and bad logic.', 'False', 'True', 'True'),
('Queen of Swords', 'Capable of powerful intellect, she says what she means, is open to new ideas and loyal to her logic.', 'Negatively she speaks to intellect pushed to the extreme, neglecting of the body and frigidity.', 'False', 'True', 'True'),
('King of Swords', 'He skillfully handles words and new ideas, he is the King of the court. He represents a just ruler, a professor - someone with great intellectual serenity. He puts his thoughts into appropriate actions.', 'Negatively he warns of slander, verbal aggression, legal errors, corrupt politics, or a cheater.', 'False', 'True', 'True'),
('Knight of Swords', 'Equipped with staggering thought and logic the Knight leaves behind the world of thinking and seeks the way of the lovers, almost like a prophet. After achieving mental perfection he seeks only the paths that have heart now. He brings good news, solutions, and the end of mental conflicts.', 'If at all, too aggressive in ones mental capacities.', 'False', 'True', 'True'),

('Ace of Wands', 'A spark of potential growth awaits you! If you need to fight you will be able.', 'Negatively, this indicates creative blocks, physical violence, abuse of power.', 'False', 'True', 'False'),
('Two of Wands', 'Passive sexual energy is contained but quite strong - the need to create is severe.', 'Negatively, this refers to a creativity that is eternally un-realized, crippling self-doubt. Intellect is in the way of creating.', 'False', 'True', 'False'),
('Three of Wands', 'Burst into the world with a springtime zest! Strong impulses and enthusiasm drives action.', ' Negatively this speaks to an aimless scattered mind and the potential to abuse power.', 'False', 'True', 'False'),
('Four of Wands', 'Desire becomes reality. Here a person has assumed their power and lives off the success of their creations. The danger is the sexual and creative stability which risks boredom and routine', 'Beware dominating attitudes or deep self doubt. Avoid weak people who hold authority.', 'False', 'True', 'False'),
('Five of Wands', 'This card drives temptation to push for more, and go beyond what is currently known. Indulging in passions can be healing.', 'Be wary of creativity that requires drugs or alcohol to manifest.', 'False', 'True', 'False'),
('Six of Wands', 'Work is a joy. We have surrendered to temptation and moved into ecstasy. Sexuality and creativity are fully experienced. The manifestation of Ki! Ready to move outward, to go from solo to paired.', 'Negatively, this card risks narcissism and a repetition of the same. You may be lacking in joy.', 'False', 'True', 'False'),
('Seven of Wands', 'This card asks for great openness and action in the pure selfless service to others. Action in creation, tangible engagement.', 'The negative impacts here are significant. This warns of true terror, pimping, torture, and destructive power.', 'False', 'True', 'False'),
('Eight of Wands', 'Scattered to focused, our full concentration makes power nonviolent. The individual radiates authority.', 'Negative reading is minimal but if anything it warns of perfectionism bordering on asphyxiation.', 'False', 'True', 'False'),
('Nine of Wands', 'Your energy will be confronted with the decision of life or death. Make no concessions, be yourself, be responsible but win or die.', 'Negatives refer to infertility and impotence.', 'False', 'True', 'False'),
('Ten of Wands', 'Creative energy has graduated, moving on to the next level, this project has reached its end.', 'Negatively a painful relinquishment of energy or the need to give up surfaces.','False', 'True', 'False'),
('Page of Wands', 'The hesitation between doing and not doing, this unsure energy needs to be channeled and directed.', 'Negatively, this warns of creative slumps and clumsiness.', 'False', 'True', 'True'),
('Queen of Wands', 'The Queen of Wands represents the satisfaction of someone living independently on her own merits. A secure existence and belief in ones creation.', 'Negatively this warns of obsession with excess and power.', 'False', 'True', 'True'),
('King of Wands', 'He has mastered his energy; vital, creative and sexual. He represents creativity in every aspect of life.', 'Negatively, he represents a tyrant, strong sex drive without love, and self obsessive issues', 'False', 'True', 'True'),
('Knight of Wands', 'This Knight embodies trust and straight forward communication. The Wands can be trusted again. After gaining control of his suit he is ready to move from the world of passions to the world of thought.', 'No negatives', 'False', 'True', 'True'),

('Ace of Cups', 'A gift of love given freely, the Ace of Cups is an overflowing chalice of love. This is a sign of great love which has not yet been employed and will color the rest of the reading.', 'Negatively this could signify jealousy, never sated neediness, suffering or a lack of affection.', 'False', 'True', 'False'),
('Two of Cups', 'Emotionally immature we may be transfixed in a state of amorous daydreams. We seek the first signs of love from others. We may feel imprisoned by love in this stage and wait for an ideal mate who resembles us. We prepare for love but with great hesitation and sentimentality. Combining of opposite forces, love is blind here when it needs more experience.', 'Negative aspects include, isolation, the inability to establish relationships, immaturity and fear of commitment.', 'False', 'True', 'False'),
('Three of Cups', 'Divine love and honeymoon feelings give way to first love. The freshness and inexperience and idealization of first love are all present here. The divine figure makes an appearance here making everything feel blessed. Should this fail, terrible disappointment awaits. In an intoxicated state we rediscover love at any age here.', 'Negatively we may be too fixated on love, destructive in our idealizations or committed to impossible love.', 'False', 'True', 'False'),
('Four of Cups', 'Love is established and stable - we build the foundations for family in the four of cups. With self confidence and trust love seems to be a practical pillar of our reality. It can, however, morph into a seeking of security which puts us in danger of entering a dominated and dominating relationship. The risk lies in expecting this divinely guided decision making.', 'Negatively this may speak to insecurity, materialistic love, smothering or lack of freedom.', 'False', 'True', 'False'),
('Five of Cups', 'Misunderstanding love here, we run the risk of engaging in a cult like euphoria which masks as love. we may discover faith and feel the need to put our loving efforts into that which is for the better of humanity.', 'This warns of blind trust, emotional imbalance, a lack of faith, or disappointment.', 'False', 'True', 'False'),
('Six of Cups', 'That soul mate we dreamed of in the two of cups becomes a reality. We engage in the noblest form of self love and recognize the divine within ourselves. This is a card of reflection, note the three stacked cups mirroring itself. A relationship built on esteem and fidelity thrives.', 'This warns of an overly pompous couple cutting themselves off from the world, withdrawal of the individual, potential narcissism, or self indulgence.', 'False', 'True', 'False'),
('Seven of Cups', 'We encounter a full manifestation of love and see this carried out in the world. We may be charitable without advertising it and feel connected to collective hive mind. We embrace the idea \"Nothing for me that is not for others\".', 'Negatively this speaks to being unhappy due to evils of the world, aggressiveness or the compulsive tendency to help others who have not requested it. This may also warn of someone who is deeply self-centered.', 'False', 'True', 'False'),
('Eight of Cups', 'As we reach a state of perfect love we find we love the past, present, future, the planet, ourselves, our neighbor, everything. There is no need to question love here - love is everything. Gracefully we come into a profound union with the divine. Become active towards earth and receptive towards the heavens.', 'Negatively we may revoke the acceptance of love, perpetually dissatisfied or encounter a strong love which seems to be giving but is really only taking.love, a full cup', 'False', 'True', 'False'),
('Nine of Cups', 'For the first time in the suit of cups we see leaves wilting. As we enter the Autumn of the heart we must go through a period of grieving. In this mourning a new dimension of love will appear. In our emotional wisdom it is time to accept the end of a cycle and let go of what has already been lived. Release emotions which used to nourish.', 'Negative aspects include emotional crisis, nostalgia, unwanted solitude, fear of lack and despair.', 'False', 'True', 'False'),
('Ten of Cups', 'At the height of our emotional maturity we seal our cups and get ready to put our love to work. This card will become the ace of pentacles and signifies a concrete action is ready to be taken.', 'If negative at all this card warns of a refusal to evolve.', 'False', 'True', 'False'),
('Page of Cups', 'To love or not to love? The Page of Cups is tempted and also terrified at the discovery of love. He represents first love full of doubts and enthusiasms. Potentially referring to someone who has not fully embraced oneself, he signifies a general lack of trust in love.', 'Negatively he warns of trauma from childhood, the emotionally immature, ghosts of exes and excessive daydreaming.', 'False', 'True', 'True'),
('Queen of Cups', 'Determined to defend her feelings, the Queen of Cups is perfectly content focusing on her emotions. Her trust is earned and she reflects divine love.', 'Negatively she can embody possessiveness, insecure attachment (dismissive or anxious), and false charity.', 'False', 'True', 'True'),
('King of Cups', 'With his heart open wide the King represents emotional maturity, generous love and joy. He could be a counselor or patron.', 'Negatively he warns of veiled hatred, narcissism, alcoholism and emotional abuse.', 'False', 'True', 'True'),
('Knight of Cups', 'For the Knight, love has reached its final form - it is a concrete force. With a heart sincerely full he offers himself up and asks for forgiveness. He will be able to transform his love into tangible creations.', 'No negatives', 'False', 'True', 'True'),

('Ace of Coins', 'Material potential is unlimited. The body, resources, territory or the position we hold in the world is the focus of this card. Direct your focus to the concrete aspects of life.', 'Be wary of hyper pre-occupation with material excess.', 'False', 'True', 'False'),
('Two of Coins', 'Plans will further the spiritualization of matter, work will soon be made tangible. There are still details to be worked out while you conserve strength for the next steps.', 'Negatively this warns of paralysis, money problems, refusal to eat and a unrealistic view of the world.', 'False', 'True', 'False'),
('Three of Coins', 'Investments produce their first returns or losses. There is a certain risk at play here.', 'Negatively beware of fertility issues and creating a monster.', 'False', 'True', 'False'),
('Four of Coins', 'The cycle of death and rebirth is constant. The body and the home similarly require constant upkeep. Do not allow things to stagnate. It is time to commit to action or lose progress, spend!', 'This wants of a stagnant econmic situation, prison, excess and weight issues.', 'False', 'True', 'False'),
('Five of Coins', 'We go from the comfort of the security in the Four of Pentacles to the desire for more in the Five. New possibilities of wealth are opening up, spend wisely and properly vet any investment right now.', 'Beware green-washing, bad doctors, a reversal of fortune, stock exchange crashes and greedy people.', 'False', 'True', 'False'),
('Six of Coins', 'Spend your money on what brings you joy. Invest in what you love. Seek balance of conflicting values and harmony in all aspects of life.', 'Beware superficial spending, money will not buy happiness right now. ', 'False', 'True', 'False'),
('Seven of Coins', 'Let the physical become spiritual and spiritual become physical. The realizing of your ideas can make you money, and help humanity. Gain material power based on awareness. Be sure your spirit and body work together.', 'Avoid destruction of the environment, drug companies and overvaluing the physical realm.', 'False', 'True', 'False'),
('Eight of Coins', 'Enjoy true wealth in all aspects of life. Your body balanced, family understanding and healthy home life speak to the potential paradise on Earth. Seek thorough understanding on the intersection of wealth and health in the spirit, mental and physical realms.', 'Move away from paralyzing beliefs around money and stop seeing poverty as inescapable.', 'False', 'True', 'False'),
('Nine of Coins', 'A material project has been completed and it is time for a new one. With material detachment it is time to start a new construction. Watch for the arrival of new material conditions, baby, new job, stroke of fortune.', 'Beware economic crisis, theft and eviction or being forced to move, birth of a new dimension', 'False', 'True', 'False'),
('Ten of Coins', 'All has been attained in the material plane and the path to prosperity ends. It is time to turn your energy to your passions and creativity.', 'Beware the clinging to a past life, denial of oneself and the feeling of wasting ones life.', 'False', 'True', 'False'),
('Page of Coins', 'The Page looks upon his wish coin but is blocked by his buried coin. He holds the potential to channel The Magician if only he could solidify his place in the world.', 'He warns of remaining inactive too long and playing carelessly with resources and life.','False', 'True', 'True'),
('Queen of Coins', 'Clinging to her money, position, health - she could deploy immense energy to keep things as they are. Whatever her situation needs she will make it happen.', 'She runs the risk of not looking beyond herself and ignoring the bigger picture to obtain what she seeks in the immediate. A fear of risk keeps us trapped.', 'False', 'True', 'True'),
('King of Coins', 'With no crown but a hat - this man knows how to make his money work for him while maintaining a spiritual connection to the Earth. His throne is outside in nature. A billionaire or a farmer he has mastered his material world.', 'Negatively he warns of fraud dirty money, bad stocks or a dealer of toxic goods', 'False', 'True', 'True'),
('Knight of Coins', 'This Knight marches beyond the superficial materials of existence and into creation. Horizons open to him and he is able to take his wealth and make something new. Literally speaking he refers to a move or a journey - a shift in the physical which connects to ones spiritual and emotional world.', 'No negatives', 'False', 'True', 'True');

# card = 'Queen of Wands' or card = 'Queen of Swords' or card = 'Five of Cups' or card = 'Fool' or card = 'Nine of Swords' or card = 'Two of Coins' or card = 'Moon' or card = 'Seven of Wands' or card = 'World' or card = 'Nine of Coins' or card = 'Seven of Cups' or card = 'Four of Swords' or card = 'Five of Wands' or card = 'Ace of Coins' or card = 'Hermit' or card = 'Ten of Cups' or card = 'Tower'
#
# card = 'King of Wands' or card = 'Seven of Swords' or card = 'Hermit' or card = 'Ace of Cups' or card = 'Two of Swords' or card = 'Six of Cups' or card = 'Seven of Wands' or card = 'Eight of Coins' or card = 'Three of Swords' or card = 'Four of Coins' or card = 'Eight of Swords' or card = 'Five of Swords' or card = 'Seven of Cups' or card = 'Two of Coins' or card = 'Knight of Coins' or card = 'Knight of Cups' or card = 'Tower' or card = 'Judgement' or card = 'Moon'
#
# card = 'Empress' or card = 'Seven of Wands' or card = 'Six of Wands' or card = 'Chariot' or card = 'Three of Coins' or card = 'Ten of Swords' or card = 'Knight of Wands' or card = 'Star' or card = 'King of Cups' or card = 'Moon' or card = 'Magician' or card = 'Knight of Coins' or card = 'Ace of Coins' or card = 'Nine of Cups' or card = 'Three of Cups' or card = 'Devil'
#
# card = 'Knight of Cups' or card = 'Five of Pentacles' or card = 'Queen of Cups' or card = 'Ace of Coins' or card = 'Two of Cups' or card = 'Four of Swords' or card = 'Seven of Coins' or card = 'Queen of Wands' or card = 'Temperance' or card = 'Lovers' or card = 'Page of Swords' or card = 'Judgement' or card = 'Four of Coins' or card = 'Eight of Cups' or card = 'Ten of Cups' or card = 'Four of Cups'
#
# card = 'Five of Cups' or card = 'Six of Cups' or card = 'Ace of Wands' or card = 'Nine of Swords' or card = 'Three of Wands' or card = 'Moon' or card = 'Emperor' or card = 'Hanged Man' or card = 'Two of Coins' or card = 'King of Coins' or card = 'Hermit' or card = 'Ten of Wands' or card = 'Ten of Coins' or card = 'High Priestess' or card = 'Magician' or card = 'Queen of Swords'
#
# 'Temperance' 'Death' 'Wheel of Fortune' 'Nine of Swords'
# 'Ten of Swords'
# 'Page of Swords'
# 'Queen of Swords'


# CREATE TABLE read_16 (
#     reading_id SERIAL PRIMARY KEY,
#     card_01 varchar(100),
#     card_02 varchar(100),
#     card_03 varchar(100),
#     card_04 varchar(100),
#     card_05 varchar(100),
#     card_06 varchar(100),
#     card_07 varchar(100),
#     card_08 varchar(100),
#     card_09 varchar(100),
#     card_10 varchar(100),
#     card_11 varchar(100),
#     card_12 varchar(100),
#     card_13 varchar(100),
#     card_14 varchar(100),
#     card_15 varchar(100),
#     card_16 varchar(100),
#     card_ex1 varchar(100),
#     card_ex2 varchar(100),
#     card_ex3 varchar(100)
# )
#
# INSERT INTO read_16(card_01, card_02, card_03, card_04, card_05, card_06, card_07, card_08, card_09, card_10, card_11, card_12, card_13, card_14, card_15, card_16, card_ex1)
# values
#
# ('Queen of Wands', 'Queen of Swords', 'Five of Cups', 'Fool', 'Nine of Swords', 'Two of Coins', 'Moon', 'Seven of Wands', 'World', 'Nine of Coins', 'Seven of Cups', 'Four of Swords', 'Five of Wands', 'Ace of Coins', 'Hermit', 'Ten of Cups', 'Tower')
#
# INSERT INTO read_16(card_01, card_02, card_03, card_04, card_05, card_06, card_07, card_08, card_09, card_10, card_11, card_12, card_13, card_14, card_15, card_16, card_ex1, card_ex2, card_ex3)
# values
#
# ('King of Wands', 'Seven of Swords', 'Hermit', 'Ace of Cups', 'Two of Swords', 'Six of Cups', 'Seven of Wands', 'Eight of Coins', 'Three of Swords', 'Four of Coins', 'Eight of Swords', 'Five of Swords', 'Seven of Cups', 'Two of Coins', 'Knight of Coins', 'Knight of Cups', 'Tower', 'Judgement', 'Moon')
#
# INSERT INTO read_16(card_01, card_02, card_03, card_04, card_05, card_06, card_07, card_08, card_09, card_10, card_11, card_12, card_13, card_14, card_15, card_16)
# values
# ('Empress', 'Seven of Wands', 'Six of Wands', 'Chariot', 'Three of Coins', 'Ten of Swords', 'Knight of Wands', 'Star', 'King of Cups', 'Moon', 'Magician', 'Knight of Coins', 'Ace of Coins', 'Nine of Cups', 'Three of Cups', 'Devil'),
# ('Knight of Cups', 'Five of Pentacles', 'Queen of Cups', 'Ace of Coins', 'Two of Cups', 'Four of Swords', 'Seven of Coins', 'Queen of Wands', 'Temperance', 'Lovers', 'Page of Swords', 'Judgement', 'Four of Coins', 'Eight of Cups', 'Ten of Cups', 'Four of Cups')
#
# ('Five of Cups', 'Six of Cups', 'Ace of Wands', 'Nine of Swords', 'Three of Wands', 'Moon', 'Emperor', 'Hanged Man', 'Two of Coins', 'King of Coins', 'Hermit', 'Ten of Wands', 'Ten of Coins', 'High Priestess', 'Magician', 'Queen of Swords')
#
#
# CREATE TABLE read_01 (
#     spd_01 boolean,
#     spd_02 boolean,
#     spd_03 boolean,
#     spd_04 boolean,
#     spd_05 boolean
# ) INHERITS card_meaning;
#


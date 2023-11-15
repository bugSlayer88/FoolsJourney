import create_deck

all_full_dict = {'Fool': 'The Fool evokes an enormous burst of evergy. Wherever he goes he brings this vital  '
                         'impulse. Charge forward!',
                 'Magician': 'A new beginning opens up to you. Make reasoning quick and set your focus. Make your '
                             'decisions and take action.',
                 'High Priestess': 'Stick to your ideals and morality. Maintain discipline, consider sobriety. '
                                   'Prepare the mind and body for the birth of something new.',
                 'Empress': 'Let your creativity guide you. Get inspired, get energized and make your dreams '
                            'reality.',
                 'Emperor': 'The Emperor asks questions of the father figure. How are you expressing your '
                            'masculine traits? Take action to make you and yours secure.',
                 'Hierophant': 'Open up to communication. Stick to traditions in action but keep the mind '
                               'receptive to new lessons. Seek out mentors and teachers.',
                 'Lovers': 'Get clear on your emotional state. Take time to question yourself and how you feel. '
                           'Which character on the card do you associate with currently?',
                 'Chariot': 'Beware inflexibility and lack of caution now. A successful conquest can be a reality, '
                            'particularly in the media',
                 'Justice': 'Distinguish subjective from objective judgements, learn to clearly say yes and no. '
                            'Wrap up any political or legal matters. You will get what you deserve.',
                 'Hermit': 'A change which cannot be avoided and must be accepted faces you. Look to an inner '
                           'solitude, go to the secret place within you for spiritual transformation.',
                 'Wheel of Fortune': 'The only constant in life is change. What goes up must come down. Your luck '
                                     'will turn around.',
                 'Strength': 'Are you holding yourself back? Are you letting your creativity out or reining it in? '
                             'Embrace your challenges.',
                 'Hanged Man': 'Do not make decisions now. Inaction will allow your intelligence to ripen. Make '
                               'this restraint your sacrifice for better opportunity.',
                 'Death': 'There is no birth without death. What do you need to mourn and express to feel peace? '
                          'Allow the energy of creation to come forward, if this is not enough - let the revolution'
                          ' out.',
                 'Temperance': 'Introduce positivity to the passions which harm. To dark add light, jealousy to '
                               'trust. Look at what imbalances you and bring in the opposite. Be cautious of vices.',
                 'Devil': 'Promises of money come in. Examine contracts carefully right now. For questions of '
                          'creativity - inspiration is within you. In all cases, let your desires guide you but '
                          'keep your head.',
                 'Tower': 'You face potential catastrophe or separation. Something less obvious is trying to reach '
                          'you - stop looking for God in the sky and find him on Earth.',
                 'Star': 'Luck, prosperity, fertility surround you. You have found your place in life. Where does '
                         'the Star spill her jars in your life? If it is in the past or into nothingness - how can '
                         'this be resolved.',
                 'Moon': 'Employ feminine qualities now. Lead with receptivity and intuition. Poorly defined '
                         'anxieties will cause you harm.',
                 'Sun': 'Good luck on all accounts. Look to the father figure for awakening the soul and the mother '
                        'figure for intelligence in the heart. The sun gives - take only what you need lest these '
                        'gifts bring misfortune.',
                 'Judgement': 'Stop going against who you are. Judgements made by humans do not matter right now. '
                              'Only God can judge you.',
                 'World': 'You reach understanding now. A perfect world, a happy marriage, worldly success, '
                          'successful birth. If the World is at the end of a reading ask what happened in your '
                          'childhood which is in the way of your success.',
                 'Ace of Wands': 'spark of potential growth',
                 'Two of Wands': 'First fruits of labor',
                 'Three of Wands': 'Burst into the world',
                 'Four of Wands': 'Sexual and creative stability which risks boredom and routine',
                 'Five of Wands': 'Temptation to push for more, pull at the veil',
                 'Six of Wands': 'Ready to move outward, to go from solo to paired',
                 'Seven of Wands': 'Action in creation, tangible engagement',
                 'Eight of Wands': 'Scattered to focused, full concentration',
                 'Nine of Wands': 'Make no concessions, be yourself, be responsible but win or die',
                 'Ten of Wands': 'Energy graduated, moving on to the next level, painful relinquishment of energy',
                 'Page of Wands': 'TEMP',
                 'Queen of Wands': 'TEMP',
                 'King of Wands': 'TEMP',
                 'Knight of Wands': 'TEMP',
                 'Ace of Coins': 'Growth of money',
                 'Two of Coins': 'Spiritualization of matter, work made tangible',
                 'Three of Coins': 'First results, fertility issues',
                 'Four of Coins': 'Must commit to action or lose progress, spend',
                 'Five of Coins': 'New possibility of wealth, spend wisely',
                 'Six of Coins': 'Balance of conflicting values, harmony in all aspects of life',
                 'Seven of Coins': 'Realizing of ideas, make your ideal',
                 'Eight of Coins': 'True wealth in all life, thorough understanding',
                 'Nine of Coins': 'Arrival of new material conditions, baby, new job, stroke of fortune, '
                                  'birth of a new dimension',
                 'Ten of Coins': 'All has been attained in the material plane',
                 'Page of Coins': 'TEMP',
                 'Queen of Coins': 'TEMP',
                 'King of Coins': 'TEMP',
                 'Knight of Coins': 'TEMP',
                 'Ace of Swords': 'A flash of insight, guidance to simplify the mind, cut the unnecessary',
                 'Two of Swords': 'Daydreams, plans, information, theories overflowing',
                 'Three of Swords': 'Discern between belief and knowing, too excitable, enthusiasm in learning',
                 'Four of Swords': 'Good at life in general, practical but shuts out matters of the heart',
                 'Five of Swords': 'False understanding of the world, dangerous polarizing, too enthusiastic',
                 'Six of Swords': 'Attain beauty from within, meditate',
                 'Seven of Swords': 'Lessons in receptivity, remove distractions',
                 'Eight of Swords': 'Emptiness, the buddhist void',
                 'Nine of Swords': 'Listen to others, there are other ideas than your own',
                 'Ten of Swords': 'The mind has achieved unity, a full understanding',
                 'Page of Swords': 'TEMP',
                 'Queen of Swords': 'TEMP',
                 'King of Swords': 'TEMP',
                 'Knight of Swords': 'TEMP',
                 'Ace of Cups': 'A gift of love given freely',
                 'Two of Cups': 'Combining of opposite forces, love is blind',
                 'Three of Cups': 'Divine love, honeymoon feelings',
                 'Four of Cups': 'Seeking outer validation, insecure in love',
                 'Five of Cups': 'Misunderstanding of love, cult like love',
                 'Six of Cups': 'soul mates, potential narcissism, love reflecting what it sees, not honest',
                 'Seven of Cups': 'Full manifestation of love',
                 'Eight of Cups': 'Active towards earth receptive towards the heavens, perfect balance, perfect '
                                  'love, a full cup',
                 'Nine of Cups': 'Release emotions which used to nourish, analyze your love',
                 'Ten of Cups': 'Nothing for me that is not for others, full heart',
                 'Page of Cups': 'TEMP',
                 'Queen of Cups': 'TEMP',
                 'King of Cups': 'TEMP',
                 'Knight of Cups': 'TEMP'
                 }

minor_key_dict = {'Ace': ['fresh start'],
                  'Two': ['decisions', 'planning'],
                  'Three': ['others influence', 'team'],
                  'Four': ['structure', 'solid foundation'],
                  'Five': ['instability', 'instigate'],
                  'Six': ['departure', 'harmony'],
                  'Seven': ['temptation', 'fatigue'],
                  'Eight': ['boundaries', 'foundation'],
                  'Nine': ['drive', 'seeking perfection'],
                  'Ten': ['extremes', 'completion'],
                  'Page': ['new messages'],
                  'Queen': ['full focus'],
                  'King': ['secure', 'peace'],
                  'Knight': ['evolution', 'suit bringer']
                  }

major_key_dict = {'Fool': ['new journey', 'unknown'],
                  'Magician': ['creation'],
                  'High Priestess': ['wisdom'],
                  'Empress': ['life', 'create'],
                  'Emperor': ['rule', 'conquer'],
                  'Hierophant': ['tradition', 'structure'],
                  'Lovers': ['love', 'decisions'],
                  'Chariot': ['movement', 'peace'],
                  'Justice': ['consequences', 'honesty', 'lessons'],
                  'Hermit': ['reflection', 'assessment'],
                  'Wheel of Fortune': ['luck', 'karma'],
                  'Strength': ['bravery', 'competence'],
                  'Hanged Man': ['sacrifice', 'let go'],
                  'Death': ['renewal', 'change'],
                  'Temperance': ['balance', 'tranquility'],
                  'Devil': ['addiction', 'obsession', 'trapped'],
                  'Tower': ['sudden upheaval', 'violence', 'chaos'],
                  'Star': ['hope', 'inspiration'],
                  'Moon': ['anxiety', 'deception', 'subconscious'],
                  'Sun': ['freedom', 'pregnancy', 'confidence'],
                  'Judgement': ['forgiveness', 'evaluation'],
                  'World': ['success', 'fulfilment', 'completion']
                  }

minor_full_dict = {'Ace of Wands': 'spark of potential growth',
                   'Two of Wands': 'First fruits of labor',
                   'Three of Wands': 'Burst into the world',
                   'Four of Wands': 'Sexual and creative stability which risks boredom and routine',
                   'Five of Wands': 'Temptation to push for more, pull at the veil',
                   'Six of Wands': 'Ready to move outward, to go from solo to paired',
                   'Seven of Wands': 'Action in creation, tangible engagement',
                   'Eight of Wands': 'Scattered to focused, full concentration',
                   'Nine of Wands': 'Make no concessions, be yourself, be responsible but win or die',
                   'Ten of Wands': 'Energy graduated, moving on to the next level, painful relinquishment of energy',
                   'Page of Wands': 'TEMP',
                   'Queen of Wands': 'TEMP',
                   'King of Wands': 'TEMP',
                   'Knight of Wands': 'TEMP',
                   'Ace of Coins': 'Growth of money',
                   'Two of Coins': 'Spiritualization of matter, work made tangible',
                   'Three of Coins': 'First results, fertility issues',
                   'Four of Coins': 'Must commit to action or lose progress, spend',
                   'Five of Coins': 'New possibility of wealth, spend wisely',
                   'Six of Coins': 'Balance of conflicting values, harmony in all aspects of life',
                   'Seven of Coins': 'Realizing of ideas, make your ideal',
                   'Eight of Coins': 'True wealth in all life, thorough understanding',
                   'Nine of Coins': 'Arrival of new material conditions, baby, new job, stroke of fortune, '
                                    'birth of a new dimension',
                   'Ten of Coins': 'All has been attained in the material plane',
                   'Page of Coins': 'TEMP',
                   'Queen of Coins': 'TEMP',
                   'King of Coins': 'TEMP',
                   'Knight of Coins': 'TEMP',
                   'Ace of Swords': 'A flash of insight, guidance to simplify the mind, cut the unnecessary',
                   'Two of Swords': 'Daydreams, plans, information, theories overflowing',
                   'Three of Swords': 'Discern between belief and knowing, too excitable, enthusiasm in learning',
                   'Four of Swords': 'Good at life in general, practical but shuts out matters of the heart',
                   'Five of Swords': 'False understanding of the world, dangerous polarizing, too enthusiastic',
                   'Six of Swords': 'Attain beauty from within, meditate',
                   'Seven of Swords': 'Lessons in receptivity, remove distractions',
                   'Eight of Swords': 'Emptiness, the buddhist void',
                   'Nine of Swords': 'Listen to others, there are other ideas than your own',
                   'Ten of Swords': 'The mind has achieved unity, a full understanding',
                   'Page of Swords': 'TEMP',
                   'Queen of Swords': 'TEMP',
                   'King of Swords': 'TEMP',
                   'Knight of Swords': 'TEMP',
                   'Ace of Cups': 'A gift of love given freely',
                   'Two of Cups': 'Combining of opposite forces, love is blind',
                   'Three of Cups': 'Divine love, honeymoon feelings',
                   'Four of Cups': 'Seeking outer validation, insecure in love',
                   'Five of Cups': 'Misunderstanding of love, cult like love',
                   'Six of Cups': 'soul mates, potential narcissism, love reflecting what it sees, not honest',
                   'Seven of Cups': 'Full manifestation of love',
                   'Eight of Cups': 'Active towards earth receptive towards the heavens, perfect balance, perfect '
                                    'love, a full cup',
                   'Nine of Cups': 'Release emotions which used to nourish, analyze your love',
                   'Ten of Cups': 'Nothing for me that is not for others, full heart',
                   'Page of Cups': 'TEMP',
                   'Queen of Cups': 'TEMP',
                   'King of Cups': 'TEMP',
                   'Knight of Cups': 'TEMP'
                   }

major_rank_dict = {'Fool': ['0'],
                   'Magician': ['1'],
                   'High Priestess': ['2'],
                   'Empress': ['3'],
                   'Emperor': ['4'],
                   'Hierophant': ['5'],
                   'Lovers': ['6'],
                   'Chariot': ['7'],
                   'Justice': ['8'],
                   'Hermit': ['9'],
                   'Wheel of Fortune': ['10'],
                   'Strength': ['Eleven'],
                   'Hanged Man': ['Twelve'],
                   'Death': ['Thirteen'],
                   'Temperance': ['Fourteen'],
                   'Devil': ['Fifteen'],
                   'Tower': ['Sixteen'],
                   'Star': ['Seventeen'],
                   'Moon': ['Eighteen'],
                   'Sun': ['Nineteen'],
                   'Judgement': ['Twenty'],
                   'World': ['Twenty One']
                   }

major_suit_dict = {'Fool': ['Wands'],
                   'Magician': ['Coins'],
                   'High Priestess': ['Swords'],
                   'Empress': ['Cups'],
                   'Emperor': ['Wands'],
                   'Hierophant': ['Coins'],
                   'Lovers': ['Swords'],
                   'Chariot': ['Cups'],
                   'Justice': ['Wands'],
                   'Hermit': ['Coins'],
                   'Wheel of Fortune': [''],
                   'Strength': ['Swords'],
                   'Hanged Man': ['Swords'],
                   'Death': ['Cups'],
                   'Temperance': ['Wands'],
                   'Devil': ['Coins'],
                   'Tower': [''],
                   'Star': ['Swords'],
                   'Moon': ['Cups'],
                   'Sun': ['Wands'],
                   'Judgement': [''],
                   'World': ['']
                   }

major_full_dict = {'Fool': 'The Fool evokes an enormous burst of evergy. Wherever he goes he brings this vital  '
                           'impulse. Charge forward!',
                   'Magician': 'A new beginning opens up to you. Make reasoning quick and set your focus. Make your '
                               'decisions and take action.',
                   'High Priestess': 'Stick to your ideals and morality. Maintain discipline, consider sobriety. '
                                     'Prepare the mind and body for the birth of something new.',
                   'Empress': 'Let your creativity guide you. Get inspired, get energized and make your dreams '
                              'reality.',
                   'Emperor': 'The Emperor asks questions of the father figure. How are you expressing your '
                              'masculine traits? Take action to make you and yours secure.',
                   'Hierophant': 'Open up to communication. Stick to traditions in action but keep the mind '
                                 'receptive to new lessons. Seek out mentors and teachers.',
                   'Lovers': 'Get clear on your emotional state. Take time to question yourself and how you feel. '
                             'Which character on the card do you associate with currently?',
                   'Chariot': 'Beware inflexibility and lack of caution now. A successful conquest can be a reality, '
                              'particularly in the media',
                   'Justice': 'Distinguish subjective from objective judgements, learn to clearly say yes and no. '
                              'Wrap up any political or legal matters. You will get what you deserve.',
                   'Hermit': 'A change which cannot be avoided and must be accepted faces you. Look to an inner '
                             'solitude, go to the secret place within you for spiritual transformation.',
                   'Wheel of Fortune': 'The only constant in life is change. What goes up must come down. Your luck '
                                       'will turn around.',
                   'Strength': 'Are you holding yourself back? Are you letting your creativity out or reining it in? '
                               'Embrace your challenges.',
                   'Hanged Man': 'Do not make decisions now. Inaction will allow your intelligence to ripen. Make '
                                 'this restraint your sacrifice for better opportunity.',
                   'Death': 'There is no birth without death. What do you need to mourn and express to feel peace? '
                            'Allow the energy of creation to come forward, if this is not enough - let the revolution'
                            ' out.',
                   'Temperance': 'Introduce positivity to the passions which harm. To dark add light, jealousy to '
                                 'trust. Look at what imbalances you and bring in the opposite. Be cautious of vices.',
                   'Devil': 'Promises of money come in. Examine contracts carefully right now. For questions of '
                            'creativity - inspiration is within you. In all cases, let your desires guide you but '
                            'keep your head.',
                   'Tower': 'You face potential catastrophe or separation. Something less obvious is trying to reach '
                            'you - stop looking for God in the sky and find him on Earth.',
                   'Star': 'Luck, prosperity, fertility surround you. You have found your place in life. Where does '
                           'the Star spill her jars in your life? If it is in the past or into nothingness - how can '
                           'this be resolved.',
                   'Moon': 'Employ feminine qualities now. Lead with receptivity and intuition. Poorly defined '
                           'anxieties will cause you harm.',
                   'Sun': 'Good luck on all accounts. Look to the father figure for awakening the soul and the mother '
                          'figure for intelligence in the heart. The sun gives - take only what you need lest these '
                          'gifts bring misfortune.',
                   'Judgement': 'Stop going against who you are. Judgements made by humans do not matter right now. '
                                'Only God can judge you.',
                   'World': 'You reach understanding now. A perfect world, a happy marriage, worldly success, '
                            'successful birth. If the World is at the end of a reading ask what happened in your '
                            'childhood which is in the way of your success.'
                   }

modality_dict = {'Wands': 'Active',
                 'Swords': 'Active',
                 'Coins': 'Receptive',
                 'Cups': 'Receptive',
                 'Fool': 'Neutral',
                 'Magician': 'Active',
                 'High Priestess': 'Receptive',
                 'Empress': 'Receptive',
                 'Emperor': 'Active',
                 'Hierophant': 'Receptive',
                 'Lovers': 'Active',
                 'Chariot': 'Receptive',
                 'Justice': 'Active',
                 'Hermit': 'Receptive',
                 'Wheel of Fortune': 'Receptive',
                 'Strength': 'Active',
                 'Hanged Man': 'Receptive',
                 'Death': 'Receptive',
                 'Temperance': 'Active',
                 'Devil': 'Receptive',
                 'Tower': 'Receptive',
                 'Star': 'Active',
                 'Moon': 'Receptive',
                 'Sun': 'Active',
                 'Judgement': 'Receptive',
                 'World': 'Active'
                 }

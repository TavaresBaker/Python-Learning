import random

# === Static category pools ===
special_characters = list("!@#$%^&*()-_+=[]{}`~|\\:;'<>,.?/")

numbers = [str(num) for num in range(10, 100)]

# Placeholder lists, fill these with your actual data
verbs = [
    "accept", "ache", "acknowledge", "act", "add", "admire", "admit", "admonish", "adopt", "advise",
    "affirm", "afford", "agree", "ail", "alert", "allege", "allow", "allude", "amuse", "analyze",
    "announce", "annoy", "answer", "apologize", "appeal", "appear", "applaud", "appreciate", "approve", "argue",
    "arrange", "arrest", "arrive", "articulate", "ask", "assert", "assure", "attach", "attack", "attempt",
    "attend", "attract", "auction", "avoid", "avow", "awake", "babble", "back", "bake", "balance",
    "balk", "ban", "bandage", "bang", "bar", "bare", "bargain", "bark", "barrage", "barter",
    "baste", "bat", "bathe", "battle", "bawl", "be", "beam", "bear", "beat", "become",
    "befriend", "beg", "begin", "behave", "believe", "bellow", "belong", "bend", "berate", "besiege",
    "bestow", "bet", "bid", "bite", "bleach", "bleed", "bless", "blind", "blink", "blot",
    "blow", "blurt", "blush", "boast", "bob", "boil", "bolt", "bomb", "book", "bore",
    "borrow", "bounce", "bow", "box", "brag", "brake", "branch", "brand", "break", "breathe",
    "breed", "bring", "broadcast", "broil", "bruise", "brush", "bubble", "build", "bump", "burn",
    "burnish", "bury", "buy", "buzz", "cajole", "calculate", "call", "camp", "care", "carry",
    "carve", "catch", "cause", "caution", "challenge", "change", "chant", "charge", "chase", "cheat",
    "check", "cheer", "chew", "chide", "chip", "choke", "chomp", "choose", "chop", "claim",
    "clap", "clean", "clear", "climb", "clip", "close", "coach", "coil", "collect", "color",
    "comb", "come", "comfort", "command", "comment", "communicate", "compare", "compete", "complain", "complete",
    "concede", "concentrate", "concern", "conclude", "concur", "confess", "confide", "confirm", "connect", "consent",
    "consider", "consist", "contain", "contend", "continue", "cook", "copy", "correct", "cost", "cough",
    "count", "counter", "cover", "covet", "crack", "crash", "crave", "crawl", "criticize", "croak",
    "crochet", "cross", "cross-examine", "crowd", "crush", "cry", "cure", "curl", "curse", "curve",
    "cut", "cycle", "dam", "damage", "dance", "dare", "deal", "debate", "decay", "deceive",
    "decide", "decipher", "declare", "decorate", "delay", "delight", "deliver", "demand", "deny", "depend",
    "describe", "desert", "deserve", "desire", "deter", "develop", "dial", "dictate", "die", "dig",
    "digress", "direct", "disclose", "dislike", "dive", "divide", "divorce", "divulge", "do", "dock",
    "dole", "dote", "double", "doubt", "drag", "drain", "draw", "dream", "dress", "drill",
    "drink", "drip", "drive", "drone", "drop", "drown", "dry", "dump", "dupe", "dust",
    "dye", "earn", "eat", "echo", "edit", "educate", "elope", "embarrass", "emigrate", "emit",
    "emphasize", "employ", "empty", "enchant", "encode", "encourage", "end", "enjoin", "enjoy", "enter",
    "entertain", "enunciate", "envy", "equivocate", "escape", "evacuate", "evaporate", "exaggerate", "examine", "excite",
    "exclaim", "excuse", "exercise", "exhort", "exist", "expand", "expect", "expel", "explain", "explode",
    "explore", "extend", "extol", "face", "fade", "fail", "fall", "falter", "fasten", "favor",
    "fax", "fear", "feed", "feel", "fence", "fetch", "fight", "file", "fill", "film",
    "find", "fire", "fish", "fit", "fix", "flap", "flash", "flee", "float", "flood",
    "floss", "flow", "flower", "fly", "fold", "follow", "fool", "force", "foretell", "forget",
    "forgive", "form", "found", "frame", "freeze", "fret", "frighten", "fry", "fume", "garden",
    "gasp", "gather", "gaze", "gel", "get", "gild", "give", "glide", "glue", "gnaw",
    "go", "grab", "grate", "grease", "greet", "grill", "grin", "grip", "groan", "grow",
    "growl", "grumble", "grunt", "guarantee", "guard", "guess", "guide", "gurgle", "gush", "hail",
    "hammer", "hand", "handle", "hang", "happen", "harass", "harm", "harness", "hate", "haunt",
    "have", "head", "heal", "heap", "hear", "heat", "help", "hide", "highlight", "hijack",
    "hinder", "hint", "hiss", "hit", "hold", "hook", "hoot", "hop", "hope", "hover",
    "howl", "hug", "hum", "hunt", "hurry", "hurt", "ice", "identify", "ignore", "imagine",
    "immigrate", "implore", "imply", "impress", "improve", "include", "increase", "infect", "inflate", "influence",
    "inform", "infuse", "inject", "injure", "inquire", "insist", "inspect", "inspire", "instruct", "intend",
    "interest", "interfere", "interject", "interrupt", "introduce", "invent", "invest", "invite", "iron", "irritate",
    "itch", "jab", "jabber", "jail", "jam", "jeer", "jest", "jog", "join", "joke",
    "jolt", "judge", "juggle", "jump", "keep", "kick", "kill", "kiss", "kneel", "knit",
    "knock", "knot", "know", "label", "lament", "land", "last", "laugh", "lay", "lead",
    "lean", "learn", "leave", "lecture", "lend", "let", "level", "license", "lick", "lie",
    "lift", "light", "lighten", "like", "list", "listen", "live", "load", "loan", "lock",
    "long", "look", "loosen", "lose", "love", "lower", "mail", "maintain", "make", "man",
    "manage", "mar", "march", "mark", "marry", "marvel", "mate", "matter", "mean", "measure",
    "meet", "melt", "memorize", "mend", "mention", "merge", "milk", "mine", "miss", "mix",
    "moan", "molt", "moor", "mourn", "move", "mow", "mug", "multiply", "mumble", "murder",
    "mutter", "nag", "nail", "name", "nap", "need", "nest", "nod", "note", "notice",
    "number", "obey", "object", "observe", "obtain", "occur", "offend", "offer", "ogle", "oil",
    "omit", "open", "operate", "order", "overflow", "overrun", "owe", "own", "pack", "pad",
    "paddle", "paint", "pant", "park", "part", "pass", "paste", "pat", "pause", "pay",
    "peck", "pedal", "peel", "peep", "peer", "peg", "pelt", "perform", "permit", "pester",
    "pet", "phone", "pick", "pinch", "pine", "place", "plan", "plant", "play", "plead",
    "please", "pledge", "plow", "plug", "point", "poke", "polish", "ponder", "pop", "possess",
    "post", "postulate", "pour", "practice", "pray", "preach", "precede", "predict", "prefer", "prepare",
    "present", "preserve", "press", "pretend", "prevent", "prick", "print", "proceed", "proclaim", "produce",
    "profess", "program", "promise", "propose", "protect", "protest", "provide", "pry", "pull", "pump",
    "punch", "puncture", "punish", "push", "put", "question", "quilt", "quit", "quiz", "quote",
    "race", "radiate", "rain", "raise", "rant", "rate", "rave", "reach", "read", "realize",
    "rebuff", "recall", "receive", "recite", "recognize", "recommend", "record", "reduce", "reflect", "refuse",
    "regret", "reign", "reiterate", "reject", "rejoice", "relate", "relax", "release", "rely", "remain",
    "remember", "remind", "remove", "repair", "repeat", "replace", "reply", "report", "reprimand", "reproduce",
    "request", "rescue", "retire", "retort", "return", "reveal", "reverse", "rhyme", "ride", "ring",
    "rinse", "rise", "risk", "roar", "rob", "rock", "roll", "rot", "row", "rub",
    "ruin", "rule", "run", "rush", "sack", "sail", "satisfy", "save", "savor", "saw",
    "say", "scare", "scatter", "scoff", "scold", "scoot", "scorch", "scrape", "scratch", "scream",
    "screech", "screw", "scribble", "seal", "search", "see", "sell", "send", "sense", "separate",
    "serve", "set", "settle", "sever", "sew", "shade", "shampoo", "share", "shave", "shelter",
    "shift", "shiver", "shock", "shoot", "shop", "shout", "show", "shriek", "shrug", "shut",
    "sigh", "sign", "signal", "sin", "sing", "singe", "sip", "sit", "skate", "skateboard",
    "sketch", "ski", "skip", "slap", "sleep", "slice", "slide", "slip", "slow", "smash",
    "smell", "smile", "smoke", "snap", "snarl", "snatch", "sneak", "sneer", "sneeze", "snicker",
    "sniff", "snoop", "snooze", "snore", "snort", "snow", "soak", "sob", "soothe", "sound",
    "sow", "span", "spare", "spark", "sparkle", "speak", "speculate", "spell", "spend", "spill",
    "spin", "spoil", "spot", "spray", "sprout", "sputter", "squash", "squeeze", "stab", "stain",
    "stammer", "stamp", "stand", "star", "stare", "start", "stash", "state", "stay", "steer",
    "step", "stipulate", "stir", "stitch", "stop", "store", "storm", "stow", "strap", "stray",
    "strengthen", "stress", "stretch", "strip", "stroke", "strum", "strut", "stuff", "stun", "stunt",
    "stutter", "submerge", "succeed", "suffer", "suggest", "suit", "supply", "support", "suppose", "surmise",
    "surprise", "surround", "suspect", "suspend", "sway", "swear", "swim", "swing", "switch", "swoop",
    "sympathize", "take", "talk", "tame", "tap", "taste", "taunt", "teach", "tear", "tease",
    "telephone", "tell", "tempt", "terrify", "test", "testify", "thank", "thaw", "theorize", "think",
    "threaten", "throw", "thunder", "tick", "tickle", "tie", "time", "tip", "tire", "toast",
    "toss", "touch", "tour", "tow", "trace", "track", "trade", "train", "translate", "transport",
    "trap", "travel", "treat", "tremble", "trick", "trickle", "trim", "trip", "trot", "trouble",
    "trounce", "trust", "try", "tug", "tumble", "turn", "twist", "type", "understand", "undress",
    "unfasten", "unite", "unlock", "unpack", "untie", "uphold", "upset", "upstage", "urge", "use",
    "usurp", "utter", "vacuum", "value", "vanish", "vanquish", "venture", "visit", "voice", "volunteer",
    "vote", "vouch", "wail", "wait", "wake", "walk", "wallow", "wander", "want", "warm",
    "warn", "wash", "waste", "watch", "water", "wave", "waver", "wear", "weave", "wed",
    "weigh", "welcome", "whimper", "whine", "whip", "whirl", "whisper", "whistle", "win", "wink",
    "wipe", "wish", "wobble", "wonder", "work", "worry", "wrap", "wreck", "wrestle", "wriggle",
    "write", "writhe", "x-ray", "yawn", "yell", "yelp", "yield", "yodel", "zip", "zoom"
]

adjectives = [
    "abandoned", "able", "absolute", "academic", "acceptable", "acclaimed", "accomplished", "accurate", "aching", "acidic",
    "acrobatic", "active", "actual", "adept", "admirable", "admired", "adolescent", "adorable", "adored", "advanced",
    "adventurous", "affectionate", "afraid", "aged", "aggravating", "aggressive", "agile", "agitated", "agonizing", "agreeable",
    "ajar", "alarmed", "alarming", "alert", "alienated", "alive", "all", "altruistic", "amazing", "ambitious",
    "ample", "amused", "amusing", "anchored", "ancient", "angelic", "angry", "anguished", "animated", "annual",
    "another", "antique", "anxious", "any", "apprehensive", "appropriate", "apt", "arctic", "arid", "aromatic",
    "artistic", "ashamed", "assured", "astonishing", "athletic", "attached", "attentive", "attractive", "austere", "authentic",
    "authorized", "automatic", "avaricious", "average", "aware", "awesome", "awful", "awkward", "babyish", "back",
    "bad", "baggy", "bare", "barren", "basic", "beautiful", "belated", "beloved", "beneficial", "best",
    "better", "bewitched", "big", "big-hearted", "biodegradable", "bite-sized", "bitter", "black", "black-and-white", "bland",
    "blank", "blaring", "bleak", "blind", "blissful", "blond", "blue", "blushing", "bogus", "boiling",
    "bold", "bony", "boring", "bossy", "both", "bouncy", "bountiful", "bowed", "brave", "breakable",
    "brief", "bright", "brilliant", "brisk", "broken", "bronze", "brown", "bruised", "bubbly", "bulky",
    "bumpy", "buoyant", "burdensome", "burly", "bustling", "busy", "buttery", "buzzing", "calculating", "calm",
    "candid", "canine", "capital", "carefree", "careful", "careless", "caring", "cautious", "cavernous", "celebrated",
    "charming", "cheap", "cheerful", "cheery", "chief", "chilly", "chubby", "circular", "classic", "clean",
    "clear", "clear-cut", "clever", "close", "closed", "cloudy", "clueless", "clumsy", "cluttered", "coarse",
    "cold", "colorful", "colorless", "colossal", "comfortable", "common", "compassionate", "competent", "complete", "complex",
    "complicated", "composed", "concerned", "concrete", "confused", "conscious", "considerate", "constant", "content", "conventional",
    "cooked", "cool", "cooperative", "coordinated", "corny", "corrupt", "costly", "courageous", "courteous", "crafty",
    "crazy", "creamy", "creative", "creepy", "criminal", "crisp", "critical", "crooked", "crowded", "cruel",
    "crushing", "cuddly", "cultivated", "cultured", "cumbersome", "curly", "curvy", "cute", "cylindrical", "damaged",
    "damp", "dangerous", "dapper", "daring", "dark", "darling", "dazzling", "dead", "deadly", "deafening",
    "dear", "dearest", "decent", "decimal", "decisive", "deep", "defenseless", "defensive", "defiant", "deficient",
    "definite", "definitive", "delayed", "delectable", "delicious", "delightful", "delirious", "demanding", "dense", "dental",
    "dependable", "dependent", "descriptive", "deserted", "detailed", "determined", "devoted", "different", "difficult", "digital",
    "diligent", "dim", "dimpled", "dimwitted", "direct", "dirty", "disastrous", "discrete", "disfigured", "disguised",
    "disgusting", "dishonest", "disloyal", "dismal", "distant", "distinct", "distorted", "dizzy", "dopey", "doting",
    "double", "downright", "drab", "drafty", "dramatic", "dreary", "droopy", "dry", "dual", "dull",
    "dutiful", "eager", "early", "earnest", "easy", "easy-going", "ecstatic", "edible", "educated", "elaborate",
    "elastic", "elated", "elderly", "electric", "elegant", "elementary", "elliptical", "embarrassed", "embellished", "eminent",
    "emotional", "empty", "enchanted", "enchanting", "energetic", "enlightened", "enormous", "enraged", "entire", "envious",
    "equal", "equatorial", "essential", "esteemed", "ethical", "euphoric", "even", "evergreen", "everlasting", "every",
    "evil", "exalted", "excellent", "excitable", "excited", "exciting", "exemplary", "exhausted", "exotic", "expensive",
    "experienced", "expert", "extra-large", "extra-small", "extraneous", "extroverted", "fabulous", "failing", "faint", "fair",
    "faithful", "fake", "false", "familiar", "famous", "fancy", "fantastic", "far", "far-flung", "far-off",
    "faraway", "fast", "fat", "fatal", "fatherly", "favorable", "favorite", "fearful", "fearless", "feisty",
    "feline", "female", "feminine", "few", "fickle", "filthy", "fine", "finished", "firm", "first",
    "firsthand", "fitting", "fixed", "flaky", "flamboyant", "flashy", "flat", "flawed", "flawless", "flickering",
    "flimsy", "flippant", "flowery", "fluffy", "fluid", "flustered", "focused", "fond", "foolhardy", "foolish",
    "forceful", "forked", "formal", "forsaken", "forthright", "fortunate", "fragrant", "frail", "frank", "frayed",
    "free", "French", "frequent", "fresh", "friendly", "frightened", "frightening", "frigid", "frilly", "frivolous",
    "frizzy", "front", "frosty", "frozen", "frugal", "fruitful", "full", "fumbling", "functional", "funny",
    "fussy", "fuzzy", "gargantuan", "gaseous", "general", "generous", "gentle", "genuine", "giant", "giddy",
    "gifted", "gigantic", "giving", "glamorous", "glaring", "glass", "gleaming", "gleeful", "glistening", "glittering",
    "gloomy", "glorious", "glossy", "glum", "golden", "good", "good-natured", "gorgeous", "graceful", "gracious",
    "grand", "grandiose", "granular", "grateful", "grave", "gray", "great", "greedy", "green", "gregarious",
    "grim", "grimy", "gripping", "grizzled", "gross", "grotesque", "grouchy", "grounded", "growing", "growling",
    "grown", "grubby", "gruesome", "grumpy", "guilty", "gullible", "gummy", "hairy", "half", "handmade",
    "handsome", "handy", "happy", "happy-go-lucky", "hard", "hard-to-find", "harmful", "harmless", "harmonious", "harsh",
    "hasty", "hateful", "haunting", "healthy", "heartfelt", "hearty", "heavenly", "heavy", "hefty", "helpful",
    "helpless", "hidden", "hideous", "high", "high-level", "hilarious", "hoarse", "hollow", "homely", "honest",
    "honorable", "honored", "hopeful", "horrible", "hospitable", "hot", "huge", "humble", "humiliating", "humming",
    "humongous", "hungry", "hurtful", "husky", "icky", "icy", "ideal", "idealistic", "identical", "idiotic",
    "idle", "idolized", "ignorant", "ill", "ill-fated", "ill-informed", "illegal", "illiterate", "illustrious", "imaginary",
    "imaginative", "immaculate", "immaterial", "immediate", "immense", "impartial", "impassioned", "impeccable", "imperfect", "imperturbable",
    "impish", "impolite", "important", "impossible", "impractical", "impressionable", "impressive", "improbable", "impure", "inborn",
    "incomparable", "incompatible", "incomplete", "inconsequential", "incredible", "indelible", "indolent", "inexperienced", "infamous", "infantile",
    "infatuated", "inferior", "infinite", "informal", "innocent", "insecure", "insidious", "insignificant", "insistent", "instructive",
    "insubstantial", "intelligent", "intent", "intentional", "interesting", "internal", "international", "intrepid", "ironclad", "irresponsible",
    "irritating", "itchy", "jaded", "jagged", "jam-packed", "jaunty", "jealous", "jittery", "joint", "jolly",
    "jovial", "joyful", "joyous", "jubilant", "judicious", "juicy", "jumbo", "jumpy", "junior", "juvenile",
    "kaleidoscopic", "keen", "key", "kind", "kindhearted", "kindly", "klutzy", "knobby", "knotty", "knowing",
    "knowledgeable", "known", "kooky", "kosher", "lame", "lanky", "large", "last", "lasting", "late", "lavish", "lawful", "lazy", "leading",
    "leafy", "lean", "left", "legal", "legitimate", "light", "lighthearted", "likable", "likely", "limited",
    "limp", "limping", "linear", "lined", "liquid", "little", "lively", "livid", "loathsome", "lone",
    "lonely", "long", "long-term", "loose", "lopsided", "lost", "loud", "lovable", "lovely", "loving",
    "low", "loyal", "lucky", "lumbering", "luminous", "lumpy", "lustrous", "luxurious", "mad", "made-up",
    "magnificent", "majestic", "major", "male", "mammoth", "married", "marvelous", "masculine", "massive", "mature",
    "meager", "mealy", "mean", "measly", "meaty", "medical", "mediocre", "medium", "meek", "mellow",
    "melodic", "memorable", "menacing", "merry", "messy", "metallic", "mild", "milky", "mindless", "miniature",
    "minor", "minty", "miserable", "miserly", "misguided", "misty", "mixed", "modern", "modest", "moist",
    "monstrous", "monthly", "monumental", "moral", "mortified", "motherly", "motionless", "mountainous", "muddy", "muffled",
    "multicolored", "mundane", "murky", "mushy", "musty", "muted", "mysterious", "naive", "narrow", "nasty",
    "natural", "naughty", "nautical", "near", "neat", "necessary", "needy", "negative", "neglected", "negligible",
    "neighboring", "nervous", "new", "next", "nice", "nifty", "nimble", "nippy", "nocturnal", "noisy",
    "nonstop", "normal", "notable", "noted", "noteworthy", "novel", "noxious", "numb", "nutritious", "nutty",
    "obedient", "obese", "oblong", "obvious", "occasional", "odd", "oddball", "offbeat", "offensive", "official",
    "oily", "old", "old-fashioned", "only", "open", "optimal", "optimistic", "opulent", "orange", "orderly",
    "ordinary", "organic", "original", "ornate", "ornery", "other", "our", "outgoing", "outlandish", "outlying",
    "outrageous", "outstanding", "oval", "overcooked", "overdue", "overjoyed", "overlooked", "palatable", "pale", "paltry",
    "parallel", "parched", "partial", "passionate", "past", "pastel", "peaceful", "peppery", "perfect", "perfumed",
    "periodic", "perky", "personal", "pertinent", "pesky", "pessimistic", "petty", "phony", "physical", "piercing",
    "pink", "pitiful", "plain", "plaintive", "plastic", "playful", "pleasant", "pleased", "pleasing", "plump",
    "plush", "pointed", "pointless", "poised", "polished", "polite", "political", "poor", "popular", "portly",
    "posh", "positive", "possible", "potable", "powerful", "powerless", "practical", "precious", "present", "prestigious",
    "pretty", "previous", "pricey", "prickly", "primary", "prime", "pristine", "private", "prize", "probable",
    "productive", "profitable", "profuse", "proper", "proud", "prudent", "punctual", "pungent", "puny", "pure",
    "purple", "pushy", "putrid", "puzzled", "puzzling", "quaint", "qualified", "quarrelsome", "quarterly", "queasy",
    "querulous", "questionable", "quick", "quick-witted", "quiet", "quintessential", "quirky", "quixotic", "quizzical", "radiant",
    "ragged", "rapid", "rarer", "rash", "raw", "ready", "real", "realistic", "reasonable", "recent",
    "reckless", "rectangular", "red", "reflecting", "regal", "regular", "reliable", "relieved", "remarkable", "remorseful",
    "remote", "repentant", "repulsive", "required", "respectful", "responsible", "revolving", "rewarding", "rich", "right",
    "rigid", "ringed", "ripe", "roasted", "robust", "rosy", "rotating", "rotten", "rough", "round",
    "rowdy", "royal", "rubbery", "ruddy", "ruder", "rundown", "runny", "rural", "rusty", "sad",
    "safe", "salty", "same", "sandy", "saner", "sarcastic", "sardonic", "satisfied", "scaly", "scarce",
    "scared", "scary", "scented", "scholarly", "scientific", "scornful", "scratchy", "scrawny", "second", "second-hand",
    "secondary", "secret", "self-assured", "self-reliant", "selfish", "sentimental", "separate", "serene", "serious", "serpentine",
    "several", "severe", "shabby", "shadowy", "shady", "shallow", "shameful", "shameless", "sharp", "shimmering",
    "shiny", "shocked", "shocking", "shoddy", "short", "short-term", "showy", "shrill", "shy", "sick",
    "silent", "silky", "silly", "simple", "sincere", "skinny", "sleepy", "slight", "slimy", "slippery",
    "slow", "small", "smart", "smoggy", "smooth", "smug", "soft", "solid", "somber", "sore",
    "sour", "Spanish", "sparkling", "spicy", "spiky", "spiritual", "spiteful", "splendid", "spotless", "square",
    "squeaky", "staking", "stalwart", "standard", "stark", "steady", "steep", "sticky", "stiff", "stimulating",
    "stingy", "stormy", "strange", "strict", "striking", "striped", "strong", "stunning", "stupid", "sturdy",
    "subdued", "submissive", "substantial", "successful", "succulent", "sudden", "sugary", "sunny", "super", "superb",
    "superficial", "superior", "supportive", "suppressed", "sure-footed", "surprised", "suspicious", "svelte", "sweet", "swift",
    "sympathetic", "systematic", "taboo", "tacit", "tacky", "talented", "talkative", "tall", "tame", "tan",
    "tangible", "tart", "tasteful", "tasty", "tawdry", "tearful", "tedious", "teeming", "tempting", "tender",
    "tense", "tepid", "terrible", "terrific", "testy", "thankful", "that", "these", "thick", "thin",
    "third", "thirsty", "thorough", "thorny", "thoughtful", "threadbare", "thrifty", "thunderous", "tidy", "tight",
    "timely", "tinted", "tiny", "tired", "toothsome", "torpid", "tough", "traumatic", "treasured", "tremendous",
    "tricky", "trifling", "trim", "trivial", "troubled", "true", "trusting", "trustworthy", "truthful", "tubby",
    "turbulent", "turquoise", "twin", "ugly", "ultimate", "ultra", "unacceptable", "unaware", "uncomfortable", "uncommon",
    "unconscious", "understated", "unequaled", "uneven", "unfinished", "unfit", "unfolded", "unfortunate", "unhappy", "unhealthy",
    "uniform", "unimportant", "unique", "united", "unkempt", "unknown", "unlawful", "unlined", "unlucky", "unnatural",
    "unpleasant", "unrealistic", "unripe", "unselfish", "unsightly", "unsophisticated", "unstable", "unsung", "untidy", "untimely",
    "untried", "untrue", "unused", "unusual", "unwieldy", "unwilling", "unwise", "upbeat", "upright", "upset",
    "urban", "usable", "used", "useful", "useless", "utilized", "utter", "vacant", "vague", "vain",
    "valid", "valuable", "vapid", "variable", "varied", "vast", "velvety", "venerated", "vengeful", "venomous",
    "verdant", "versatile", "vibrant", "vicious", "victorious", "vigilant", "vigorous", "violent", "virgin", "virtual",
    "virtuous", "visible", "vital", "vivacious", "vivid", "voiceless", "volatile", "voluminous", "voracious", "vulgar",
    "vulnerable", "wacky", "waggish", "waiting", "wakeful", "wandering", "wanting", "warlike", "warm", "warmhearted",
    "warped", "wary", "wasteful", "watchful", "waterlogged", "waterproof", "watery", "weak", "wealthy", "weary",
    "webbed", "wee", "weekly", "weepy", "weighty", "weird", "welcome", "well-documented", "well-groomed", "well-informed",
    "well-lit", "well-made", "well-off", "well-to-do", "well-worn", "wet", "whimsical", "whispered", "white", "whole",
    "whopping", "wicked", "wide", "wide-eyed", "wiggly", "wild", "willing", "wilted", "winding", "windy",
    "winged", "wiry", "wise", "witty", "wobbly", "woeful", "wonderful", "wooden", "woozy", "workable",
    "worried", "worrisome", "worthless", "worthy", "wrathful", "wretched", "wrong", "wry", "yawning", "yearly",
    "yellow", "young", "youthful", "yummy", "zany", "zealous", "zesty", "zigzag", "zippy", "zonal"
]

colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "gray",
    "cyan", "magenta", "violet", "indigo", "turquoise", "teal", "lime", "maroon", "navy", "olive",
    "gold", "silver", "bronze", "beige", "coral", "crimson", "azure", "amber", "burgundy", "chartreuse",
    "cerulean", "cobalt", "fuchsia", "lavender", "mint", "mustard", "peach", "plum", "salmon", "scarlet",
    "tan", "taupe", "topaz", "ultramarine", "vermilion", "wheat", "periwinkle", "saffron", "emerald", "opal",
    "ruby", "sapphire", "jade", "ivory", "charcoal", "carmine", "denim", "eggplant", "firebrick", "heliotrope",
    "khaki", "lemon", "mauve", "ochre", "pistachio", "quartz", "rosewood", "sepia", "smoke", "tangerine",
    "viridian", "zaffre", "celadon", "ebony", "ginger", "harlequin", "iris", "jasper", "kelly", "lapis",
    "mandarin", "nebula", "onyx", "peacock", "quince", "raspberry", "sangria", "tulip", "umber", "verdigris",
    "xanadu", "yarrow", "zaffre"
]


statics = [special_characters, numbers]
optional_statics = [verbs, adjectives, colors]

# === Theme lists ===
superheros = [
    "SpiderMan", "IronMan", "CaptainAmerica", "Thor", "Hulk", "BlackWidow", "DoctorStrange", "BlackPanther", "CaptainMarvel", "AntMan",
    "Wolverine", "Deadpool", "Cyclops", "Storm", "JeanGrey", "ProfessorX", "Magneto", "Gambit", "Nightcrawler", "Colossus",
    "Daredevil", "JessicaJones", "LukeCage", "IronFist", "GhostRider", "SilverSurfer", "Nova", "ScarletWitch", "Quicksilver", "Vision",
    "Falcon", "Hawkeye", "WinterSoldier", "StarLord", "Gamora", "Drax", "RocketRaccoon", "Groot", "Venom", "Carnage",
    "Deadshot", "HarleyQuinn", "Batman", "Superman", "WonderWoman", "Flash", "GreenLantern", "Aquaman", "Cyborg", "GreenArrow",
    "MartianManhunter", "BlackCanary", "Shazam", "Nightwing", "Batgirl", "Robin", "Constantine", "SwampThing", "BlueBeetle", "Hawkman",
    "DoctorFate", "Zatanna", "Supergirl", "BlackLightning", "RedHood", "Starfire", "Raven", "BeastBoy", "Terra", "JohnStewart",
    "JessicaCruz", "KateKane", "PlasticMan", "CaptainAtom", "BoosterGold", "Vixen", "AnimalMan", "TheAtom", "Firestorm", "RedTornado",
    "Hellboy", "Spawn", "JudgeDredd", "Invincible", "OmniMan", "AtomEve", "Tera", "Glory", "WallyWest", "JayGarrick",
    "BlueLantern", "SquirrelGirl", "MsMarvel", "SheHulk", "LukeCage", "IronFist", "JessicaDrew", "NovaSamAlexander", "KateBishop", "MilesMorales",
    "KamalaKhan", "RiriWilliams", "Iceman", "Magik", "Cable", "Psylocke", "EmmaFrost", "Rogue", "Gambit", "Bishop",
    "Static", "Icon", "Rocket", "NightThrasher", "SpiderGwen", "Silk", "MoonKnight", "Cloak", "Dagger", "Hercules",
    "DoctorDoom", "Loki", "Thanos", "Galactus", "Apocalypse", "Darkseid", "Brainiac", "Sinestro", "Ultron", "RedSkull",
    "Mystique", "Deathstroke", "RaAlGhul", "Bane", "BlackManta", "CaptainCold", "ReverseFlash", "Zoom", "SolomonGrundy", "GeneralZod",
    "Rorschach", "NiteOwl", "SilkSpectre", "TheComedian", "Ozymandias", "HitGirl", "KickAss", "JohnConstantine", "Saitama", "Goku",
    "Vegeta", "NarutoUzumaki", "SasukeUchiha", "IchigoKurosaki", "Luffy", "Zoro", "Todoroki", "Bakugo", "AllMight", "Deku",
    "Shoto", "Midoriya", "Kamina", "Simon", "YusukeUrameshi", "Genos", "Garou", "TengenToppaGurrenLagann", "SilverSamurai", "Blade",
    "MoonGirl", "BlueMarvel", "MisterFantastic", "InvisibleWoman", "HumanTorch", "TheThing", "StaticShock", "MsAmerica", "PowerGirl", "Huntress",
    "Batwoman", "BlackCat", "NovaRichardRider", "CaptainBritain", "Hellcat", "Moonstone", "WarMachine", "Quake", "DaisyJohnson", "PhilCoulson",
    "CaptainUniverse", "ShangChi", "SpiderWoman", "WonderMan", "Sentry", "BetaRayBill", "RedHulk", "SheThing", "ElsaBloodstone", "DoctorVoodoo",
    "Songbird", "BlackKnight", "Mockingbird", "Mantis", "Nebula", "Yondu", "BlueDevil", "Fire", "Ice", "Vibe",
    "Katana", "Wildcat", "MrTerrific", "Zauriel", "Azrael", "Question", "MisterMiracle", "BigBarda", "Orion", "Lightray",
    "Metamorpho", "BlackAdam", "CaptainMarvelJr", "MaryMarvel", "Spectre", "GreenLanternHalJordan", "GreenLanternJohnStewart", "GreenLanternKyleRayner",
    "GreenLanternJessicaCruz", "GreenLanternSimonBaz", "SinestroCorps", "RedLanterns", "StarSapphireCorps", "BlackLanterns", "FlashBarryAllen", "FlashWallyWest",
    "FlashJayGarrick", "Impulse", "KidFlash", "JesseQuick", "RobinDickGrayson", "RobinJasonTodd", "RobinTimDrake", "RobinDamianWayne", "RedHood", "BatgirlBarbaraGordon",
    "BatgirlCassandraCain", "Spoiler", "Orphan", "Hawkgirl", "BlackLightning", "BlueBeetleJaimeReyes", "CaptainCold", "HeatWave", "MirrorMaster", "GorillaGrodd",
    "CaptainBoomerang", "TheTrickster", "Zoom", "ReverseFlash", "SolomonGrundy", "Deadshot", "Joker", "LexLuthor", "Darkseid", "Brainiac",
    "Bane", "RaAlGhul", "BlackManta", "CaptainNazi", "KillerCroc", "LadyShiva", "Giganta", "Cheetah", "BlackMask", "Blackfire",
    "DoctorPolaris", "Parasite", "Prometheus", "WeatherWizard", "Juggernaut", "Okoye", "MoonKnight", "Ironheart", "BlueBeetle", "Icon",
    "Hardware", "TheRay", "GreenArrow", "BlueDevil", "Firestorm", "BoosterGold"
]

games = [
    "Minecraft", "Fortnite", "CallOfDuty", "LeagueOfLegends", "ApexLegends", "Valorant", "Overwatch", "CounterStrike", "AmongUs", "FallGuys",
    "WorldOfWarcraft", "Destiny2", "GodOfWar", "TheWitcher3", "RedDeadRedemption2", "Cyberpunk2077", "GrandTheftAutoV", "AssassinsCreed", "EldenRing", "DarkSouls3",
    "FIFA23", "RocketLeague", "SuperSmashBros", "MarioKart", "AnimalCrossing", "TheLegendOfZelda", "HollowKnight", "Celeste", "StardewValley", "DeadByDaylight",
    "PUBG", "MinecraftDungeons", "Terraria", "Fallout4", "Skyrim", "TheLastOfUs", "GodOfWarRagnarok", "HaloInfinite", "Battlefield2042", "RainbowSixSiege",
    "Dota2", "MinecraftBedrock", "TheDivision2", "GenshinImpact", "Valorant", "Overcooked", "Cuphead", "OriAndTheWillOfTheWisps", "MassEffect", "BioShock",
    "CivilizationVI", "Fallout76", "AmongUs", "ForzaHorizon5", "DeadSpace", "DiabloIII", "LeagueOfLegendsWildRift", "TheElderScrollsOnline", "MarioParty", "Splatoon3",
    "Tekken7", "StreetFighterV", "MonsterHunterRise", "FireEmblem", "Persona5", "DeadCells", "Hades", "Portal2", "HalfLife2", "Left4Dead2",
    "Cyberpunk2077", "MinecraftJava", "Subnautica", "Rust", "ARKSurvivalEvolved", "Valorant", "Overwatch2", "Destiny2", "GTAOnline", "FallGuysUltimateKnockout",
    "AmongUs", "CallOfDutyWarzone", "LeagueOfLegends", "FortniteBattleRoyale", "RocketLeague", "MinecraftModded", "HollowKnightSilksong", "FIFA22", "MaddenNFL22", "SuperMarioOdyssey",
    "AnimalCrossingNewHorizons", "TheLegendOfZeldaBreathOfTheWild", "FinalFantasy7Remake", "Persona4", "Bayonetta", "DragonAge", "Battlefield1", "Warframe", "Valorant", "Overwatch",
    "CallOfDutyBlackOps", "DarkSouls", "Sekiro", "GhostOfTsushima", "TheLastGuardian", "Bloodborne", "Cuphead", "OriAndTheBlindForest", "Splatoon2", "Smite",
    "TeamFortress2", "MinecraftStoryMode", "StarCraftII", "Hearthstone", "MagicTheGatheringArena", "CivilizationV", "StardewValley", "Terraria", "Factorio", "SubnauticaBelowZero",
    "Brawlhalla", "Paladins", "ClashRoyale", "MobileLegends", "LeagueOfLegends", "Valorant", "Overwatch", "Fortnite", "CallOfDutyMobile", "MinecraftPocketEdition"
]

randomness = [
    "chill", "easy", "basic", "moderate", "mixed", "balanced", "varied", "wild", "chaotic", "full-throttle",
    "calm", "steady", "brisk", "breezy", "spry", "nimble", "lively", "fiery", "fierce", "ferocious",
    "mild", "spicy", "zesty", "peppered", "robust", "vigorous", "tempest", "stormy", "turbulent", "tempestuous",
    "lazy", "sluggish", "drowsy", "dozy", "lethargic", "random", "erratic", "unpredictable", "volatile", "wildcard",
    "madcap", "berserk", "insane", "lunatic", "maniacal", "unstoppable", "reckless", "breakneck", "full-speed", "all-in"
]

movies = [
    "StarWars", "TheGodfather", "TheDarkKnight", "PulpFiction", "Inception", "TheMatrix", "FightClub", "ForrestGump", "LordOfTheRings", "AvengersEndgame",
    "JurassicPark", "Titanic", "Gladiator", "Interstellar", "TheShawshankRedemption", "TheSilenceOfTheLambs", "TheLionKing", "BackToTheFuture", "TheWizardOfOz", "Frozen",
    "HarryPotter", "SpiderMan", "IronMan", "BlackPanther", "CaptainAmerica", "ThorRagnarok", "GuardiansOfTheGalaxy", "Deadpool", "WonderWoman", "BatmanBegins",
    "Aquaman", "TheIncredibles", "ToyStory", "FindingNemo", "StarTrek", "PiratesOfTheCaribbean", "TheHungerGames", "TheJurassicWorld", "TheMatrixReloaded", "TheMatrixRevolutions",
    "Transformers", "Shrek", "TheAvengers", "DoctorStrange", "AntMan", "CaptainMarvel", "BladeRunner", "Jumanji", "Kingsman", "TheExorcist",
    "TheDeparted", "DjangoUnchained", "MadMaxFuryRoad", "TheGrandBudapestHotel", "LaLaLand", "TheSocialNetwork", "BlackWidow", "TheLionKing2019", "Coco", "Moana",
    "Up", "InsideOut", "Zootopia", "Wonder", "Joker", "Logan", "Deadpool2", "GuardiansOfTheGalaxyVol2", "AvengersInfinityWar", "StarWarsTheForceAwakens",
    "TheDarkKnightRises", "SpiderManFarFromHome", "SpiderManNoWayHome", "DoctorStrangeMultiverse", "Frozen2", "ToyStory4", "CaptainMarvel", "BlackPantherWakanda", "ThorLoveAndThunder", "TheBatman",
    "TheIrishman", "InglouriousBasterds", "OnceUponATimeInHollywood", "Parasite", "GetOut", "Us", "ItChapterTwo", "TheConjuring", "Annabelle", "Saw",
    "TheHobbit", "TheLordOfTheRingsTheFellowshipOfTheRing", "TheLordOfTheRingsTheTwoTowers", "TheLordOfTheRingsTheReturnOfTheKing", "HarryPotterAndTheSorcerersStone", "HarryPotterAndTheChamberOfSecrets", "HarryPotterAndThePrisonerOfAzkaban", "HarryPotterAndTheGobletOfFire", "HarryPotterAndTheOrderOfThePhoenix", "HarryPotterAndTheHalfBloodPrince",
    "HarryPotterAndTheDeathlyHallowsPart1", "HarryPotterAndTheDeathlyHallowsPart2", "TheMartian", "Gravity", "TheBigLebowski", "ThePrestige", "TheWolfOfWallStreet", "TheGreenMile", "SavingPrivateRyan", "SchindlersList",
    "TheUsualSuspects", "Alien", "Aliens", "TheTerminator", "Terminator2JudgmentDay", "Avatar", "Inception", "Dunkirk", "BladeRunner2049", "LaLaLand"
]

tv_shows = [
    "BreakingBad", "GameOfThrones", "StrangerThings", "TheWalkingDead", "TheOfficeUS", "Friends", "RickAndMorty", "Westworld", "TheSimpsons", "BetterCallSaul",
    "Sherlock", "TheBigBangTheory", "HouseOfCards", "Dexter", "Lost", "Narcos", "BlackMirror", "TrueDetective", "TheCrown", "PeakyBlinders",
    "Suits", "TheWitcher", "Arrow", "TheFlash", "Supernatural", "Lucifer", "AgentsOfSHIELD", "HowIMetYourMother", "Vikings", "TheBoys",
    "Ozark", "Homeland", "Mindhunter", "TheMandolorian", "TheWire", "MadMen", "Fargo", "Community", "BrooklynNineNine", "RickAndMorty",
    "TheHandmaidsTale", "StrangerThingsSeason3", "TheExpanse", "BoJackHorseman", "BetterThings", "BlackList", "TheGoodPlace", "MrRobot", "House", "LostInSpace",
    "DowntonAbbey", "TheSimpsons", "SpongeBobSquarePants", "TheWestWing", "24TwentyFour", "Fringe", "PersonOfInterest", "BuffyTheVampireSlayer", "TheXFiles", "Arrowverse",
    "CurbYourEnthusiasm", "GilmoreGirls", "OrphanBlack", "TheUmbrellaAcademy", "Manifest", "CastleRock", "NarcosMexico", "TheLastOfUs", "TheMorningShow", "TrueBlood",
    "TheLeftovers", "BlackSails", "HouseMD", "RickAndMorty", "TedLasso", "SquidGame", "TheGoodFight", "Seinfeld", "That70sShow", "DeadToMe",
    "BrooklynNineNine", "TheFlashSeason7", "TheOA", "Castle", "Supergirl", "TheDefenders", "JessicaJones", "Daredevil", "LukeCage", "IronFist",
    "Gotham", "ThePunisher", "TheWireSeason1", "TheWireSeason2", "TheWireSeason3", "TheWireSeason4", "TheWireSeason5", "MindhunterSeason2", "TheQueenGambit", "TheHandmaidsTaleSeason3"
]

cities = [
    "NewYork", "LosAngeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "SanAntonio", "SanDiego", "Dallas", "SanJose",
    "Austin", "Jacksonville", "FortWorth", "Columbus", "Charlotte", "SanFrancisco", "Indianapolis", "Seattle", "Denver", "WashingtonDC",
    "Boston", "ElPaso", "Nashville", "Detroit", "OklahomaCity", "Portland", "LasVegas", "Memphis", "Louisville", "Baltimore",
    "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Mesa", "KansasCity", "Atlanta", "LongBeach", "ColoradoSprings",
    "Raleigh", "Miami", "VirginiaBeach", "Omaha", "Oakland", "Minneapolis", "Tulsa", "Arlington", "NewOrleans", "Wichita",
    "Cleveland", "Tampa", "Bakersfield", "Aurora", "Honolulu", "Anaheim", "SantaAna", "CorpusChristi", "Riverside", "Lexington",
    "StLouis", "Stockton", "Pittsburgh", "SaintPaul", "Cincinnati", "Anchorage", "Henderson", "Greensboro", "Plano", "Newark",
    "Lincoln", "Orlando", "Irvine", "Toledo", "JerseyCity", "ChulaVista", "Durham", "FortWayne", "StPetersburg", "Laredo",
    "Buffalo", "Madison", "Lubbock", "Chandler", "Scottsdale", "Glendale", "Reno", "Norfolk", "WinstonSalem", "NorthLasVegas",
    "Irving", "Chesapeake", "Gilbert", "Hialeah", "Garland", "Fremont", "Richmond", "Boise", "BatonRouge", "DesMoines",
    "Spokane", "SanBernardino", "Modesto", "Fontana", "SantaClarita", "Birmingham", "Oxnard", "Fayetteville", "MorenoValley", "Rochester",
    "GlendaleCA", "HuntingtonBeach", "SaltLakeCity", "GrandRapids", "Amarillo", "Yonkers", "AuroraCO", "Montgomery", "Akron", "LittleRock",
    "Huntsville", "Augusta", "PortStLucie", "GrandPrairie", "ColumbusOH", "Tallahassee", "OverlandPark", "Tempe", "McKinney", "Mobile",
    "CapeCoral", "Shreveport", "Frisco", "Knoxville", "Worcester", "Brownsville", "VancouverWA", "FortLauderdale", "SiouxFalls", "OntarioCA",
    "Chattanooga", "Providence", "NewportNews", "RanchoCucamonga", "SantaRosa", "Peoria", "Oceanside", "ElkGrove", "Salem", "PembrokePines",
    "Eugene", "GardenGrove", "Cary", "FortCollins", "CoronaCA", "Springfield", "JacksonMS", "Alexandria", "Hayward", "Clarksville",
    "Lakewood", "LancasterCA", "Salinas", "Palmdale", "HollywoodCA", "PasadenaCA", "Sunnyvale", "Macon", "KansasCityMO", "Pomona",
    "Escondido", "Killeen", "Naperville", "Joliet", "Bellevue", "Rockford", "Savannah", "Paterson", "Torrance", "Bridgeport",
    "McAllen", "Mesquite", "Syracuse", "MidlandTX", "PasadenaTX", "Murfreesboro", "Miramar", "Dayton", "Fullerton", "Olathe",
    "OrangeCA", "Thornton", "Roseville", "Denton", "Waco", "Surprise", "Carrollton", "WestValleyCity", "CharlestonSC", "ColumbiaSC",
    "Topeka", "ElizabethNJ", "GainesvilleFL", "ThorntonCO", "AlexandriaVA", "LafayetteLA", "SpringfieldMO", "CoronaNY", "SantaClara", "Victorville"
]

countries = [
    "UnitedStates", "Canada", "Mexico", "Brazil", "Argentina", "UnitedKingdom", "France", "Germany", "Italy", "Spain",
    "Russia", "China", "India", "Japan", "SouthKorea", "NorthKorea", "Australia", "NewZealand", "SouthAfrica", "Egypt",
    "Nigeria", "Kenya", "Morocco", "SaudiArabia", "UnitedArabEmirates", "Israel", "Turkey", "Iran", "Iraq", "Syria",
    "Jordan", "Lebanon", "Thailand", "Vietnam", "Indonesia", "Philippines", "Malaysia", "Singapore", "Pakistan", "Bangladesh",
    "Nepal", "Bhutan", "SriLanka", "Mongolia", "Kazakhstan", "Uzbekistan", "Turkmenistan", "Kyrgyzstan", "Tajikistan",
    "Ukraine", "Belarus", "Poland", "CzechRepublic", "Slovakia", "Hungary", "Romania", "Bulgaria", "Serbia", "Croatia",
    "BosniaAndHerzegovina", "Slovenia", "NorthMacedonia", "Albania", "Greece", "Portugal", "Iceland", "Ireland", "Belgium",
    "Netherlands", "Luxembourg", "Switzerland", "Austria", "Denmark", "Norway", "Sweden", "Finland", "Estonia", "Latvia",
    "Lithuania", "Malta", "Cyprus", "Cuba", "DominicanRepublic", "Jamaica", "Haiti", "CostaRica", "Panama", "Guatemala",
    "ElSalvador", "Honduras", "Nicaragua", "Belize", "Colombia", "Venezuela", "Peru", "Ecuador", "Bolivia", "Paraguay",
    "Uruguay", "Chile", "Guyana", "Suriname", "Bahamas", "Barbados", "TrinidadAndTobago", "SaintLucia", "Grenada",
    "SaintVincentAndTheGrenadines", "AntiguaAndBarbuda", "Dominica", "SaintKittsAndNevis", "NewCaledonia", "Fiji", "Samoa",
    "Tonga", "Vanuatu", "PapuaNewGuinea", "SolomonIslands", "Kiribati", "Tuvalu", "Nauru", "MarshallIslands", "Palau",
    "Micronesia", "Maldives", "Mauritius", "Seychelles", "Madagascar", "Zambia", "Zimbabwe", "Botswana", "Namibia",
    "Angola", "Mozambique", "Malawi", "Tanzania", "Uganda", "Rwanda", "Burundi", "SouthSudan", "Sudan", "Chad", "Niger",
    "Mali", "Senegal", "Gambia", "Guinea", "SierraLeone", "Liberia", "IvoryCoast", "Ghana", "Togo", "Benin", "BurkinaFaso",
    "CentralAfricanRepublic", "DemocraticRepublicOfCongo", "RepublicOfCongo", "EquatorialGuinea", "Gabon", "Cameroon",
    "Ethiopia", "Djibouti", "Eritrea", "Somalia", "Lesotho", "Eswatini", "Morocco", "Algeria", "Tunisia", "Libya", "WesternSahara",
    "Greenland", "Taiwan", "HongKong", "Macau", "Kosovo", "VaticanCity", "Monaco", "Liechtenstein", "SanMarino", "Andorra",
    "Malawi", "Syria", "Lebanon"
]

animals = [
    "Alligator", "Alpaca", "Antelope", "Armadillo", "Baboon", "Badger", "Barracuda", "Bat", "Beaver", "Bison",
    "Butterfly", "Camel", "Capybara", "Caribou", "Cassowary", "Cat", "Caterpillar", "Cheetah", "Chicken", "Chimpanzee",
    "Chinchilla", "Clam", "Cobra", "Cockroach", "Cougar", "Coyote", "Crab", "Crane", "Crocodile", "Crow",
    "Deer", "Dingo", "Dog", "Dolphin", "Donkey", "Dragonfly", "Duck", "Eagle", "Echidna", "Eel",
    "Elephant", "Elk", "Emu", "Falcon", "Ferret", "Finch", "Fish", "Flamingo", "Fox", "Frog",
    "Gazelle", "Gecko", "Gerbil", "Giraffe", "Goat", "Goldfish", "Goose", "Gorilla", "Grasshopper", "GreatWhiteShark",
    "Groundhog", "Grouse", "GuineaPig", "Gull", "Hamster", "Hedgehog", "Heron", "Hippopotamus", "Hornet", "Horse",
    "Hummingbird", "Hyena", "Iguana", "Impala", "Jackal", "Jaguar", "Jellyfish", "Kangaroo", "Kingfisher", "Kiwi",
    "Koala", "KomodoDragon", "Krill", "Lemur", "Leopard", "Lion", "Llama", "Lobster", "Locust", "Lynx",
    "Macaw", "Magpie", "Mantis", "Mink", "Mole", "Mongoose", "Monkey", "Moose", "Mosquito", "Moth",
    "MountainGoat", "Mouse", "Narwhal", "Newt", "Nightingale", "Octopus", "Okapi", "Opossum", "Orangutan", "Ostrich",
    "Otter", "Owl", "Ox", "Panda", "Panther", "Parrot", "Peacock", "Pelican", "Penguin", "Pheasant",
    "Pig", "Pigeon", "Porcupine", "Porpoise", "PrairieDog", "Puffin", "Quail", "Quokka", "Rabbit", "Raccoon",
    "Ram", "Rat", "Raven", "RedPanda", "Reindeer", "Rhinoceros", "Roadrunner", "Salamander", "Salmon", "Sandpiper",
    "Scorpion", "Seahorse", "Seal", "Shark", "Sheep", "Shrimp", "Skunk", "Sloth", "Snail", "Snake",
    "Sparrow", "Spider", "Spoonbill", "Squid", "Squirrel", "Starfish", "Stingray", "Stork", "Swallow", "Swan",
    "Tiger", "Toad", "Trout", "Turkey", "Turtle", "Vulture", "Wallaby", "Walrus", "Wasp", "Weasel",
    "Whale", "Wolf", "Wombat", "Woodpecker", "Wren", "Yak", "Zebra"
]

themes = {
    1: superheros,
    2: games,
    3: tv_shows,
    4: movies,
    5: cities,
    6: countries,
    7: animals,
    8: randomness
}

# === Difficulty Settings ===
difficulty_profiles = {
    1: [3, 8, 10, 0, 0],  # module_count, min_len, max_len, min_special, min_numbers
    2: [4, 10, 14, 1, 2],
    3: [5, 16, 32, 1, 2]
}

# === User Input ===
difficulty_level = int(input("Difficulty (1-3): "))
if difficulty_level not in [1, 2, 3]:
    raise ValueError("Invalid difficulty level.")

theme_choice = int(input("Theme: 1=Superheros, 2=Games, 3=TV Shows, 4=Movies, 5=Cities, 6=Countries, 7=Animals, 8=Randomness\n"))
if theme_choice not in themes:
    raise ValueError("Invalid theme selection.")

num_passwords = int(input("How many passwords do you want? "))
if num_passwords <= 0:
    raise ValueError("Must generate at least one password.")

# === Password Generation Loop ===
for _ in range(num_passwords):
    difficulty_settings = difficulty_profiles[difficulty_level]
    module_count = difficulty_settings[0]

    # Create empty modules
    modules = [[] for _ in range(module_count)]
    used_indices = []

    # Step 1: Insert one item from selected theme
    theme_pool = themes[theme_choice]
    theme_pick = random.choice(theme_pool)
    theme_slot = random.randint(0, module_count - 1)
    modules[theme_slot].append(theme_pick)
    used_indices.append(theme_slot)

    # Step 2: Insert required number of special characters and numbers
    for _ in range(difficulty_settings[3]):  # min special characters
        while True:
            i = random.randint(0, module_count - 1)
            if i not in used_indices or len(modules[i]) == 0:
                modules[i].append(random.choice(special_characters))
                used_indices.append(i)
                break

    for _ in range(difficulty_settings[4]):  # min numbers
        while True:
            i = random.randint(0, module_count - 1)
            if i not in used_indices or len(modules[i]) == 0:
                modules[i].append(random.choice(numbers))
                used_indices.append(i)
                break

    # Step 3: Fill remaining empty modules with optional statics
    for i in range(module_count):
        if not modules[i]:
            category = random.choice(optional_statics)
            if category:
                modules[i].append(random.choice(category))
            else:
                # fallback to static category
                modules[i].append(random.choice(random.choice(statics)))

    # Step 4: Combine all module pieces into a string password
    password_parts = [item for module in modules for item in module]
    random.shuffle(password_parts)  # to prevent predictable ordering
    password = "".join(password_parts)

    print(password)

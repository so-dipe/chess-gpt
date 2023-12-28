from transformers import pipeline, AutoTokenizer
from optimum.intel import OVModelForCausalLM
from google_storage import download_blobs

download_blobs(
    "sodipe-models",
    prefix='gpt2/',
    local_directory="assets/gpt2",
)

tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = "<PAD>"

model = OVModelForCausalLM.from_pretrained("assets/gpt2")

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_next_move(previous_moves):
    if len(previous_moves) > 0:
        num_moves = len(previous_moves.split(' '))
        num_tokens = len(tokenizer(previous_moves)['input_ids'])
        moves = generator(previous_moves, max_length=(num_tokens + 7))
        moves = moves[0]['generated_text'].split(' ')
        next_move = moves[num_moves]
        return next_move
    else:
        return "must enter first move"


# print(generate_next_move("d4"))
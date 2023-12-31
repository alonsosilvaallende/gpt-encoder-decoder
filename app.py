import random
import solara
import tiktoken
import pandas as pd

# Get tokenizer for gpt-4
tokenizer = tiktoken.encoding_for_model("gpt-4")

# Create dataframe mapping token IDs and tokens
df = pd.DataFrame()
df["token ID"] = range(50257)
df["token"] = [tokenizer.decode([i]) for i in range(50257)]

text1 = solara.reactive("Example text is here")
text2 = solara.reactive("")
text3 = solara.reactive("")
@solara.component
def Page():
  solara.Markdown("#GPT-4 token encoder and decoder")
  solara.Markdown("This is an educational tool for understanding how tokenization works.")
  solara.InputText("Enter text to tokenize it:", value=text1, continuous_update=True)
  tokens = tokenizer.encode(text1.value)
  spans1 = ""
  spans2 = ""
  for i, token in enumerate(tokens):
    random.seed(i)
    random_color = ''.join([random.choice('0123456789ABCDEF') for k in range(6)])
    spans1 += " " + f"<span style='font-family: helvetica; color: #{random_color}'>{token}</span>"
    spans2 += " " + f"""<span style="
        padding: 6px;
        border-right: 3px solid white;
        line-height: 3em;
        font-family: courier;
        background-color: #{random_color};
        color: white;
        position: relative;
      "><span style="
      position: absolute;
      top: 5.5ch;
      line-height: 1em;
      left: -0.5px;
      font-size: 0.45em"> {token}</span>{tokenizer.decode([token])}</span>"""
  solara.Markdown(f"{spans1}")
  solara.Markdown(f"{len(tokens)} token") if len(tokens)==1 else solara.Markdown(f"{len(tokens)} tokens")
  solara.Markdown(f'{spans2}')
  solara.InputText("Or convert space separated tokens to text:", value=text2, continuous_update=True)
  token_input = text2.value.split(' ')
  token_input = [int(span) for span in token_input if span != ""]
  text_output = tokenizer.decode(token_input)
  solara.Markdown(f'{text_output}')
  solara.Markdown("##Search tokens")
  solara.InputText("Search for a token:", value=text3, continuous_update=True)
  df_subset = df[df["token"].str.startswith(text3.value)]
  solara.Markdown(f"{df_subset.shape[0]:,} results")
  solara.DataFrame(df_subset, items_per_page=10)

Page()

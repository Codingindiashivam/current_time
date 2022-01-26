from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
         return (
        """
    <head>
        <title>Bounce Cube</title>
    </head>
    <body>
        <div class="box one"></div>
<div class="box two"></div>
<div class="box three"></div>
<div class="box four"></div>
<div class="box five"></div>
<style>
    @keyframes bounce {
  from {
    transform: translateY(0px);
  }
  to {
    transform: translateY(var(--bounce-height));
  }
}

body {
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
}

.box {
  width: 60px;
  height: 60px;
  background: var(--bg);
  border-radius: 4px;
  will-change: transform;
}

/* 
  If you're not seeing the boxes bounce, you 
  might have "reduce motion" selected in your OS! 
*/
@media (prefers-reduced-motion: no-preference) {
  .box {
    animation: 
      bounce var(--animation-duration)
      infinite alternate
      cubic-bezier(.2, .65, .6, 1);
  }
}

.box.one {
  --bg: slateblue;
  --bounce-height: -20px;
  --animation-duration: 200ms;
}
.box.two {
  --bounce-height: -30px;
  --animation-duration: 300ms;
  --bg: deeppink;
}
.box.three {
  --bounce-height: -40px;
  --animation-duration: 400ms;
  --bg: dodgerblue;
}
.box.four {
  --bg: slateblue;
  --bounce-height: -20px;
  --animation-duration: 200ms;
}
.box.five {
  --bounce-height: -40px;
  --animation-duration: 400ms;
  --bg: dodgerblue;
}
</style>
    </body>
"""
    )

if __name__ == "__main__":
    app.run(debug=True)
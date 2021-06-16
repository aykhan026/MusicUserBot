FROM python:latest

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/mastermindvrtx/Telegram-Music-Bot-SHINIGAMI_RYUK.git
RUN cd Telegram-Music-Bot-SHINIGAMI_RYUK
WORKDIR /Telegram-Music-Bot-SHINIGAMI_RYUK
RUN pip3 install -U -r requirements.txt
CMD python3 -m ֆɦɨռɨɢǟʍɨ_ʀʏʊӄ


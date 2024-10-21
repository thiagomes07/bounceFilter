// Definindo constantes e variáveis globais
const int PINO_SENSOR = A0;  // Pino do sensor VR
const float REFERENCIA = 5.0; // Tensão de referência (em volts)
const int RESOLUCAO_ADC = 1023; // Resolução do ADC (10 bits)

unsigned long tempo;

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial
}

void loop() {
  tempo = millis(); // Obtém o tempo desde o início do programa
  int leituraADC = analogRead(PINO_SENSOR); // Lê o valor do ADC

  // Converte a leitura do ADC para tensão
  float vrVolts = leituraADC * (REFERENCIA / RESOLUCAO_ADC);
  float vcVolts = REFERENCIA - vrVolts;

  // Imprime os resultados de forma organizada
  Serial.print("VC: ");
  Serial.print(vcVolts, 2);  // 2 casas decimais
  Serial.print("\t TEMPO: ");
  Serial.print(tempo);
  Serial.print(" ms\t VR: ");
  Serial.println(vrVolts, 2);  // 2 casas decimais

  delay(1000); // Atraso de 1 segundo
}
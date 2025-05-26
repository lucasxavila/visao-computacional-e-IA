# Visão Computacional e IA: Aplicações Práticas
## Parte 1 — Pesquisa Guiada: Técnicas e Algoritmos em Visão Computacional

### - Reconhecer (Detecção, classificação ou identificação de padrões ou objetos em uma imagem)
Os **algoritmos** são conjuntos de regras ou procedimentos já definidos para realizar tarefas, como *Haar Cascade* para detecção de imagens. Por outro lado os **modelos** geralmente através do aprendizado de máquina são treinados a aprenderem padrões a partir de dados, como o *CNN (redes neurais convolucionais)* que aprende a reconhecer objetos.  

**Exemplos de técnicas ou modelos:**
- HaarCascade;
- YOLO;
- CNN;
- ResNet;
- OpenPose;

**Aplicações práticas:**
Na área da saúde, CNNs são empregadas na análise de imagens médicas, como radiografias, para identificar anomalias ou doenças.

### - Reproduzir (Geração de imagens ou reconstrução com base em padrões aprendidos)**
**Algoritmos** geram imagens muitas vezes se baseando em regras matemáticas ou estatísticas, para aumentar a resolução de imagens por exemplo, pode ser usado *algoritmos de interpolação*. Já os **modelos**, são treinados para gerar novas imagens que são semelhantes a um determinado conjunto de dados de treinamento, o *GANS (Redes Generativas Adversariais)* é um exemplo que aprende a criar imagens realistas após um treinamento com imagens reais.  

**Exemplos de técnicas ou modelos:**
- GANs (e.g. StyleGAN);
- Diffusion Models;
- Autoencoders;

**Aplicações práticas:**
No contexto industrial, modelos como GANs são usados para gerar imagens de produtos em diferentes cores, estilos ou fundos, auxiliando no design e marketing.

### - Modificar (Alteração de conteúdo visual mantendo consistência)**
Os **algoritmos** são procedimentos definidos para modificar imagens, como os filtros de edição. De outro modo os **modelos** aprende a modificar as imagens de maneira mais complexa, sendo alterando o estilo de uma imagem ou até preenchendo partes faltantes de forma realista.  

**Exemplos de técnicas ou modelos:**
- GANs;
- DeepFake;
- Segmentação + Edição;
- Stable Diffusion Inpainting;

**Aplicações práticas:**
Em relação a educação, aplicativos com a modificação de imagens auxiliam estudantes a entederem processos como a mudança ambiental ou a edição genética.

## Parte 2 — Proposta de Solução: Visão Computacional para Segurança na Mineração
### 🛠 Problema a ser resolvido
> Uma mineradora está enfrentando acidentes de trabalho por não conformidade no uso de
> Equipamentos de Proteção Individual (EPI). Funcionários acessam áreas controladas e
> perigosas sem capacete, colete ou óculos, contrariando as normas da empresa. A empresa deseja
> implementar um sistema de monitoramento automatizado com alertas em tempo real para
> mitigar o problema.

### Proposta de Solução
Uma proposta de solução desse problema seria a instalação de camêras integradas com um sistema de monitoramento que utiliza de **Visão Computacional** e **Inteligência Artificial** para:
- Detectar a presença de pessoas em áreas controladas da mineradora;
- Verificar o uso correto dos EPIs obrigatórios (capacete, colete, óculos);
- Emitir alertas em tempo real em caso de não conformidade;

### Especificações Técnicas
| Item                                                        | Resposta                                                             |
|-------------------------------------------------------------|----------------------------------------------------------------------|
| Quais tecnologias ou frameworks serão usados?               | OpenCV (processamento), YOLOv8 (para detecção), TensorFlow (treinamento), Roboflow (anotação e gerenciamento de dataset), Python - Flask (para backend e alertas), MQTT (comunicação com sistema de alertas). |
| Quais tipos de dados e imagens serão necessários?           | Imagens de câmeras de segurança em áreas industriais, rotuladas com presença ou ausência de EPIs (capacete, óculos, colete). |
| Qual será o fluxo do sistema?                               | Captura de imagem → Detecção de pessoas com YOLOv8 → Classificação de uso de EPI → Geração de alerta (visual/sonoro ou via sistema). |
| Como será o treinamento do modelo?                          | Utilização de um dataset rotulado (via Roboflow) com imagens contendo trabalhadores com e sem EPI. Dados divididos entre treino/validação/teste. Treinamento supervisionado em GPU local ou em nuvem. |
| Onde o sistema será executado?                              | Preferencialmente em edge devices como NVIDIA Jetson, podendo ter apoio na nuvem para tarefas pesadas. |
|Como será feita a validação e a medição da eficácia?         | Métricas: precisão (acurácia), recall, F1-score, número de falsos positivos/negativos. Validação contínua em campo com feedback dos operadores de segurança. |

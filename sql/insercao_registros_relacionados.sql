DECLARE
  VID_JOGO NUMBER;
  VID_TIME NUMBER;
  VID_TURMA NUMBER;
BEGIN
  VID_JOGO := JOGOS_ID_SEQ.NEXTVAL;
  INSERT INTO JOGOS VALUES (VID_JOGO, TO_TIMESTAMP('20-11-2023 15:30', 'DD-MM-YYYY HH24:MI'), '79879870000176');
  
  VID_TIME := TIMES_ID_SEQ.NEXTVAL;
  VID_TURMA := TURMAS_ID_SEQ.NEXTVAL;
  INSERT INTO TURMAS VALUES (VID_TURMA, '3C', 20, '79879870000176');
  INSERT INTO TIMES VALUES (VID_TIME, 'Galo Juvenil', 'Jorge José', 'Masculino', VID_TURMA, VID_JOGO);
  
  INSERT INTO JOGADORES VALUES ('16599911700', 'Antonio José', 18, 'Goleiro', 1, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16588811701', 'William Pedro', 20, 'Atacante', 11, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16577711702', 'Sebastião Johnny', 19, 'Meio-Campo', 10, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16555511703', 'Pedro Maia', 18, 'Defensor', 5, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16522211704', 'Jorge Maria', 19, 'Lateral', 2, VID_TIME);
END;
--
DECLARE
  VID_JOGO NUMBER;
  VID_TIME NUMBER;
  VID_TURMA NUMBER;
BEGIN
  VID_JOGO := JOGOS_ID_SEQ.NEXTVAL;
  INSERT INTO JOGOS VALUES (VID_JOGO, TO_TIMESTAMP('21-11-2023 15:30', 'DD-MM-YYYY HH24:MI'), '79879870000154');
  
  VID_TIME := TIMES_ID_SEQ.NEXTVAL;
  VID_TURMA := TURMAS_ID_SEQ.NEXTVAL;
  INSERT INTO TURMAS VALUES (VID_TURMA, '3D', 22, '79879870000154');
  INSERT INTO TIMES VALUES (VID_TIME, 'Maria Bonita', 'Jorgina Pereira', 'Feminino', VID_TURMA, VID_JOGO);
  
  INSERT INTO JOGADORES VALUES ('16599911710', 'Beatriz Silva', 20, 'Goleira', 1, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16599922720', 'Jordana Penha', 20, 'Atacante', 11, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16599933733', 'Ronalda Lucas', 19, 'Meio-Campo', 8, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16599944745', 'Luisa Augusta', 18, 'Defensora', 4, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16599955734', 'Creuza Josefina', 18, 'Lateral', 3, VID_TIME);
END;
--
DECLARE
  VID_JOGO NUMBER;
  VID_TIME NUMBER;
  VID_TURMA NUMBER;
BEGIN
  VID_JOGO := JOGOS_ID_SEQ.NEXTVAL;
  INSERT INTO JOGOS VALUES (VID_JOGO, TO_TIMESTAMP('22-11-2023 16:30', 'DD-MM-YYYY HH24:MI'), '79879870000122');
  
  VID_TIME := TIMES_ID_SEQ.NEXTVAL;
  VID_TURMA := TURMAS_ID_SEQ.NEXTVAL;
  INSERT INTO TURMAS VALUES (VID_TURMA, '3B', 24, '79879870000122');
  INSERT INTO TIMES VALUES (VID_TIME, 'Os Melhores', 'João Mbappe', 'Masculino', VID_TURMA, VID_JOGO);
  
  INSERT INTO JOGADORES VALUES ('16533311712', 'Cleiton Pernambuco', 19, 'Goleiro', 11, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16544422723', 'Lázaro Jeferson', 19, 'Atacante', 11, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16533333734', 'Paulo Matias', 19, 'Meio-Campo', 9, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16544444746', 'Rodrigo Schneider', 19, 'Defensor', 5, VID_TIME);
  INSERT INTO JOGADORES VALUES ('16533355735', 'Arnold Schwarz Silva', 19, 'Lateral', 2, VID_TIME);
END;
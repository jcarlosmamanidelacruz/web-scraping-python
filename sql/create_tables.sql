-- Table: tbingresos

-- DROP TABLE tbingresos;

CREATE TABLE tbingresos
(
  ani_pos smallint,
  num_pos character varying,
  mod_ing character varying,
  esc_pro character varying,
  cod_est character varying,
  nom_ape character varying,
  esc_pri character varying,
  num_pun character varying,
  num_mer character varying,
  des_obs character varying,
  esc_seg character varying,
  can_pun numeric(10,3),
  ord_mer smallint
)
WITH (
  OIDS=FALSE
);


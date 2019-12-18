#ifndef PROJECT_CONF_H_
#define PROJECT_CONF_H_

#define ENERGEST_CONF_ON 1

/* USB serial takes space, free more space elsewhere */
#define SICSLOWPAN_CONF_FRAG 0
// default 1280
#define UIP_CONF_BUFFER_SIZE 160

/* 
 * since we are insterested on the consumption only after network convergence,
 * it's useful to speed up the joining process
 */
// default (uint8_t[]){ 15, 20, 25, 26 }
#define TSCH_CONF_DEFAULT_HOPPING_SEQUENCE (uint8_t[]){ 25 }

#endif /* PROJECT_CONF_H_ */

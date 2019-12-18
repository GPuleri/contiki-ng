#include <stdio.h>
#include "contiki.h"
#include "sys/energest.h"
#include "sys/stimer.h"
#include "tsch.h"

PROCESS(project1_2, "project1_2");
AUTOSTART_PROCESSES(&project1_2);
/*---------------------------------------------------------------------------*/
static inline unsigned long
to_seconds(uint64_t time) {
   return (unsigned long)(time / ENERGEST_SECOND);
}
/*---------------------------------------------------------------------------*/
/*
 * This Process will periodically print energest values for the last minute.
 *
 */
PROCESS_THREAD(project1_2, ev, data) {
   static struct etimer periodic_timer;
   static struct stimer eval_timer;
   static bool start = true;

   PROCESS_BEGIN();

   etimer_set(&periodic_timer, CLOCK_SECOND);

   while (1) {
      PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&periodic_timer));
      etimer_reset(&periodic_timer);

      struct tsch_neighbor *nbr = tsch_queue_get_time_source(); // get the root's address
      if (nbr != NULL) { // check if the leaf node has joined the network

         if (start) {
            start = false;
            energest_init();
            printf("\nConnection established, start the timer for 1 min..\n");
            stimer_set(&eval_timer, 60); // Start the timer.
         }

         if (!start && stimer_expired(&eval_timer)) {
            printf("\nEnd of program\n");
            break;
         }

         /*
          * Update all energest times. Should always be called before energest
          * times are read.
          */
         energest_flush();

         printf("\nEnergest:\n");
         printf(" CPU          %4lus LPM      %4lus DEEP LPM %4lus  Total time %lus\n",
            to_seconds(energest_type_time(ENERGEST_TYPE_CPU)),
            to_seconds(energest_type_time(ENERGEST_TYPE_LPM)),
            to_seconds(energest_type_time(ENERGEST_TYPE_DEEP_LPM)),
            to_seconds(ENERGEST_GET_TOTAL_TIME()));
         printf(" Radio LISTEN %4lus TRANSMIT %4lus OFF      %4lus\n",
            to_seconds(energest_type_time(ENERGEST_TYPE_LISTEN)),
            to_seconds(energest_type_time(ENERGEST_TYPE_TRANSMIT)),
            to_seconds(ENERGEST_GET_TOTAL_TIME() -
               energest_type_time(ENERGEST_TYPE_TRANSMIT) -
               energest_type_time(ENERGEST_TYPE_LISTEN)));
      }
   }

   PROCESS_END();

}
/*---------------------------------------------------------------------------*/

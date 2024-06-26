package br.com.alura.ecommerce;

import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.common.serialization.StringDeserializer;


import java.time.Duration;
import java.util.Properties;
import java.util.Collections;

public class FraudDetectorService {
    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092"); // Endereço dos brokers Kafka
        properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG, FraudDetectorService.class.getSimpleName());
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());

        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);

        // Subscrever a um tópico
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));

        // Loop de leitura de mensagens
        while (true) {
            ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100)); // Poll para buscar registros
            if(!records.isEmpty()){
                System.out.printf("\n%d encontrados!", records.count());

                for (ConsumerRecord<String, String> record : records) {
                    System.out.println("\n--------------------------------------------------------------\n");
                    System.out.printf("Recebido registro: key=%s, value=%s, partition=%d, offset=%d%n\n",
                            record.key(), record.value(), record.partition(), record.offset());
                    try {
                        Thread.sleep(5000);
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        }



    }
}

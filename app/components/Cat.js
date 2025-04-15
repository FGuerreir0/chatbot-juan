import { motion } from "framer-motion";
import Image from 'next/image'

export default function Cat({ isSpeaking }) {
  return (
    <div className="cat-wrapper">
        <Image
          src={"/juan.webp"}
          alt="Juan the Cat"
          width={340}
          height={340}
          className="cat-image"
        />
            {isSpeaking && (
            <motion.div
              className="cat-mouth"
              animate={{ scaleY: [1, 1.3, 1] }}
              transition={{ repeat: Infinity, duration: 0.3 }}
            />
          )}
        </div>
  );
}
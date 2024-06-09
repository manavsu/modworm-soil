<script lang="ts">
  import '$lib/app.css';
</script>

<style lang="postcss">
  :global(html) {
    @apply bg-white text-black;
    caret-color: black;
  }

  @media (prefers-color-scheme: dark) {
    :global(html) {
      @apply bg-black text-white;
      caret-color: white;
    }
  }

  :global(.input) {
    @apply hover:scale-110 border-black bg-white focus:scale-110 focus:outline-none active:text-white transition duration-300 rounded-xl dark:bg-black dark:border-white;
  }

  :global(.clickable) {
    @apply hover:scale-110 active:scale-110 active:bg-black active:text-white transition duration-300 rounded-xl dark:border-white dark:bg-black dark:active:text-black dark:active:bg-white;
  }
</style>

<div class="flex flex-col h-dvh">
  <div class="flex flex-row justify-center">
    <a class="px-4" href="/network">network</a>
    <a class="px-4" href="/tables">tables</a>
  </div>
  <div class="flex-grow flex flex-row border">
      <div class="flex-grow border">
          <slot />
      </div>
  </div>
</div>
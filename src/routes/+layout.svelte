<script lang="ts">
  import '$lib/app.css';
	import { Working } from '$lib/store';
  import LoadingSnake from '$lib/loading_snake.svelte';
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
    @apply hover:scale-110 bg-white focus:scale-110 focus:outline-none active:text-white transition duration-300 rounded-xl dark:bg-black;
  }

  :global(.clickable) {
    @apply hover:scale-110 active:scale-110 active:bg-black active:text-white transition duration-300 rounded-xl dark:bg-black dark:active:text-black dark:active:bg-white;
  }
</style>

<div class="flex flex-row h-dvh">
  <div class="flex flex-col">
    <div class="flex flex-col justify-center grow">
      <a class="px-4" href="/network">network</a>
      <a class="px-4" href="/tables">tables</a>
    </div>
    <div class="mx-auto min-h-16">
      {#if $Working}
        <LoadingSnake radius={1}/>
      {/if}
    </div>
  </div>
  <div class="flex-grow flex flex-col border overscroll-contain overflow-auto">
          <slot />
  </div>
</div>